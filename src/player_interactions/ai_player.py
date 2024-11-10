import random

from src.card import Card
from src.hand import Hand
from src.player import Player
from src.table import Table

from src.player_interaction import PlayerInteraction


class Bot(PlayerInteraction):
    @classmethod
    def choose_card(cls, hand: Hand, top: Card, hand_counts: list[int] | None = None) -> Card:
        chosen_card = random.choice(hand.cards)
        return chosen_card

    @classmethod
    def choose_row(cls, table: Table, player: Player) -> int:
        row_number = random.randint(0, len(table.rows) - 1)
        print(f"{player} забирает ряд {row_number + 1}")
        return row_number

    @classmethod
    def inform_card_chosen(cls, player: Player):
        """
        Сообщает, что игрок выбрал карту.
        """
        pass

    @classmethod
    def inform_row_chosen(cls, player: Player, row: int):
        """
        Сообщает, что игрок выбрал ряд.
        """
        pass