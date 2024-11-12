import inspect
import json

from src.deck import Deck
from src.game_state import GameState
from src.hand import Hand
from src.player import Player
from src.table import Table
from src.player_interaction import PlayerInteraction
import src.player_interactions as all_player_types
import enum



class GamePhase(enum.StrEnum):
    CHOOSE_CARD = "Choose card"
    DEAL_CARDS = "Deal cards"
    CHOOSE_ROW = "Choose row"
    DISPLAY_TABLE = "Display table state"
    NEXT_PLAYER = "Switch current player"
    PLACE_CARD = "Place card"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"


class GameServer:
    INITIAL_HAND_SIZE = 10
    CHOSEN_CARD = {} #словарь хранящий значения Игрок: выбранная карта
    def __init__(self, player_types, game_state):
        self.game_state: GameState = game_state
        self.player_types: dict = player_types  # {player: PlayerInteractions}
        self.stroke_number = 0


    @classmethod
    def load_game(cls):
        filename = 'korova006.json'
        with open(filename, 'r') as fin:
            data = json.load(fin)
            game_state = GameState.load(data)
            print(game_state.save())
            player_types = {}
            for player, player_data in zip(game_state.players, data['players']):
                kind = player_data['kind']
                kind = getattr(all_player_types, kind)
                player_types[player] = kind
            return GameServer(player_types=player_types, game_state=game_state)


    def save(self):
        filename = 'korova006.json'
        data = self.save_to_dict()
        with open(filename, 'w') as fout:
            json.dump(data, fout, indent=4)


    def save_to_dict(self):
        data = self.game_state.save()
        for player_index, player in enumerate(self.player_types.keys()):
            player_interaction = self.player_types[player]
            data["players"][player_index]["kind"] = self.player_types[player].__name__
        return data


    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        names_count = {}  # для хранения счетчиков имен игроков
        for _ in range(player_count):
            name, kind = cls.request_player()

            if name in names_count:
                names_count[name] += 1
                new_name = name+str(names_count[name])
                print(f"Имя {name} было изменено на {new_name}")
            else:
                names_count[name] = 1
                new_name = name
            player = Player(new_name, Hand())
            player_types[player] = kind
        return player_types


    @classmethod
    def new_game(cls, player_types: dict):
        deck = Deck(cards=None)
        table = Table()
        for row in table: # заполнение стола первыми картами
            row.add_card(deck.draw_card())
        game_state = GameState(list(player_types.keys()), deck, table)

        res = cls(player_types, game_state)
        res.deal_cards_phase()
        return res


    def run(self):
        phases = {
            GamePhase.DEAL_CARDS: self.deal_cards_phase,
            GamePhase.DISPLAY_TABLE: self.display_table_state,
            GamePhase.CHOOSE_CARD: self.choose_card_phase,
            GamePhase.NEXT_PLAYER: self.next_player_phase,
            GamePhase.PLACE_CARD: self.place_card_phase,
            GamePhase.DECLARE_WINNER: self.declare_winner_phase,
        }
        current_phase = GamePhase.DISPLAY_TABLE
        while current_phase != GamePhase.GAME_END:
            current_phase = phases[current_phase]()


    def inform_all(self, method: str, *args, **kwargs):
        for p in self.player_types.values():
            getattr(p, method)(*args, **kwargs)


    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                player_count = int(input("How many players?"))
                if 2 <= player_count <= 10:
                    return player_count
            except ValueError:
                pass
            print("Please input a number between 2 and 10")


    @staticmethod
    def request_player() -> (str, PlayerInteraction):
        player_types = []
        for name, cls in inspect.getmembers(all_player_types):
            if inspect.isclass(cls) and issubclass(cls, PlayerInteraction):
                player_types.append(cls.__name__)
        player_types_as_str = ', '.join(player_types)

        while True:
            name = input("How to call a player?")
            if name.isalpha():
                break
            print("Name must be a single word, alphabetic characters only")

        while True:
            try:
                kind = input(f"What kind of player is it ({player_types_as_str})?")
                kind = getattr(all_player_types, kind)
                break
            except AttributeError:
                print(f"Allowed player types are: {player_types_as_str}")
        return name, kind


    def deal_cards_phase(self):
        for _ in range(self.INITIAL_HAND_SIZE):
            for p in self.player_types.keys():
                p.hand.add_card(self.game_state.deck.draw_card())
        print("Карты разданы игрокам.")
        return GamePhase.DISPLAY_TABLE


    def display_table_state(self):
        self.stroke_number += 1
        if self.stroke_number <= self.INITIAL_HAND_SIZE:
            print(f"\n****ХОД {self.stroke_number}****\nСостояние стола:\n"
                  f"{self.game_state.table} \nИгроки выбирают карту")
            return GamePhase.CHOOSE_CARD
        else:
            return GamePhase.DECLARE_WINNER


    def choose_card_phase(self) -> GamePhase:  # игроки выбирают карты

        current_player = self.game_state.current_player()
        print(f"Ход игрока: {current_player.name}({current_player.score})")  # убрать

        card = self.player_types[current_player].choose_card(current_player.hand, self.game_state.table)
        self.inform_all("inform_card_chosen", current_player)
        if card:
            print(f"{current_player.name}({current_player.score}): выбирает карту {card}")
            self.CHOSEN_CARD[current_player] = card

        if len(self.CHOSEN_CARD) == len(self.player_types):
            return GamePhase.PLACE_CARD
        else:
            return GamePhase.NEXT_PLAYER


    def next_player_phase(self) -> GamePhase:
        if self.stroke_number <= self.INITIAL_HAND_SIZE:
            self.game_state.next_player()
            return GamePhase.CHOOSE_CARD
        else:
            return GamePhase.DECLARE_WINNER


    def place_card_phase(self) -> GamePhase:

        print("\n--- Раскрытие выбранных карт ---")
        for player, card in self.CHOSEN_CARD.items():
            print(f"{player.name}({player.score}): {card}")
        print("----------------------------------")

        for player, card in sorted(self.CHOSEN_CARD.items(), key=lambda x: int(repr(x[1]))): # НАДА ПОМЕНЯТЬ !!!!!!!!!
            print(f'{player.name}({player.score}): добавление карты {card}')
            try:
                try_to_play = self.game_state.play_card(card, player)
                if try_to_play:
                    print(f'Карта игрока {player.name}({player.score}) успешно добавлена в ряд стола')
                else:
                    print(f"Картe игрока {player.name}({player.score}) не возможно добавить на стол.")
                    row_index = self.player_types[player].choose_row(self.game_state.table, player)
                    self.inform_all("inform_row_chosen", player, row_index)
                    points = self.game_state.table.rows[row_index].truncate()
                    player.score += points
                    print(f"{player.name}({player.score}): забирает ряд {row_index + 1}.")
                    print(f"\tКарта {card} становится 1-й в ряду {row_index + 1}")
                    self.game_state.table.rows[row_index].add_card(card)
                    player.hand.remove_card(card)
                    self.inform_all("inform_card_played", card)
            except ValueError as e:
                print(str(e))

        self.display_table_state()
        self.CHOSEN_CARD = {}
        return GamePhase.NEXT_PLAYER


    def declare_winner_phase(self) -> GamePhase:
        print("\nИгра закончена! Результаты игры: ")
        for player in sorted(self.game_state.players, key=lambda x:(x.score)):
            name_player = player.name
            score_player = player.score
            print(name_player, score_player)
        return GamePhase.GAME_END


def __main__():
    load_from_file = False
    if load_from_file:
        server = GameServer.load_game()
        server.save()
    else:
        server = GameServer.new_game(GameServer.get_players())
    server.run()


if __name__ == "__main__":
    __main__()