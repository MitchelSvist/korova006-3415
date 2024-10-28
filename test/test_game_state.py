import pytest
import json
from src.deck import Deck
from src.game_state import GameState
from src.player import Player
from src.table import Table

data = {
    "table": {
    "row1": "5 12",
    "row2": "6",
    "row3": "80",
    "row4": "24",
    },
    "deck": "",
    "current_player_index": 0,
    "players": [
        {
        "name": "Misha",
        "hand": "53 13 15 18 55 77 100 20 22 9",
        "score":0
        },
        {
        "name": "Bot",
        "hand": "10 11 103 44 14 62 72 73 75 1",
        "score":0
        }
    ]
}

Misha = Player.load(data["players"][0])
Bot = Player.load(data["players"][1])
full_deck = Deck(None)
json_data = json.dumps(data)
table = Table.load(json.loads(json_data)["table"])


@pytest.fixture()
def game():
    return GameState(players=[Misha, Bot], deck=full_deck, table=table, current_player=0)


def test_init(game):
    assert game.players == [Misha, Bot]
    assert game.deck == full_deck
    assert game.current_player().name == "Misha"


def test_current_player(game):
    game._current_player = 0
    assert game.current_player().name == "Misha"
    assert game._current_player == 0

    game._current_player = 1
    assert game.current_player().name == "Bot"
    assert game._current_player == 1


def test_eq(game):
    game2 = GameState(players=[Misha, Bot], deck=full_deck, table=table, current_player=0)
    game3 = GameState(players=[Misha, Bot], deck=Deck([]), table=table, current_player=1)
    assert game == game2
    assert game != game3


def test_save(game):
    expected = {
        "table": data["table"],
        "deck": str(full_deck),
        "current_player_index": 0,
        "players": [player.save() for player in game.players],
    }
    assert game.save() == expected


def test_load():
    loaded_game = GameState.load(data)
    assert loaded_game.save() == data


def test_next_player(game):
    assert game.current_player().name == "Misha"
    game.next_player()
    assert game.current_player().name == "Bot"
    game.next_player()
    assert game.current_player().name == "Misha"
