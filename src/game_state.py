from src.card import Card
from src.deck import Deck
from src.player import Player
from src.table import Table


class GameState:
    """{
  table:{
  "row1": "5",
  "row2": "6",
  "row3": "80",
  "row4": "24",
  }
  "deck": "",
  "current_player_index": 0,
  "players": [
    {
      "name": "Misha",
      "hand": "53 13 15 18 55 77 100 20 22 9",
      "is_human": True
      "score":0
    },
    {
      "name": "Bot",
      "hand": "10 11 103 44 14 62 72 73 75 1",
      "is_human": False
      "score":0
    }
  ]
}"""
    def __init__(
        self, players: list[Player], deck: Deck, table: Table, current_player: int = 0
        ):
        self.players: list[Player] = players
        self.deck: Deck = deck
        self.table: Table = table
        self._current_player: int = current_player

    def __eq__(self, other):
        return self.players == other.players and self.deck == other.deck and self.table == other.table and \
                self._current_player == other._current_player

    def current_player(self) -> Player:
        return self.players[self._current_player]

    def save(self) -> dict:
        return {
            "table": {f"row{i + 1}": self.table[i].save() for i in range(len(self.table.rows))},
            "deck": str(self.deck),
            "current_player_index": self._current_player,
            "players": [p.save() for p in self.players],
        }

    @classmethod
    def load(cls, data: dict):
        players = [Player.load(p) for p in data["players"]]

        return cls(
            players=players,
            deck=Deck.load(data["deck"]),
            table=Table.load(data["table"]),
            current_player=int(data["current_player_index"]),
        )

    def next_player(self):
        """Ход переходит к следующему игроку."""
        n = len(self.players)
        self._current_player = (self._current_player + 1) % n