import random
from src.card import Card
from src.hand import Hand
from src.player import Player
from src.table import Table

from src.player_interaction import PlayerInteraction


class Human(PlayerInteraction):
    @classmethod
    def choose_card(cls, hand: Hand, table: Table, hand_counts: list[int] | None = None) -> Card:
        """Здесь выбор карты из руки"""
        while True:
            try:
                print("Ваши карты: ", hand)
                card_int = int(input("Введите номер карты: "))
                card = Card.load(card_int)
                # hand.cards.remove(card)
                return card
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер карты ")


    @classmethod
    def choose_row(cls, table: Table, player: Player) -> int:
        """Здесь выбор ряда, который забирает игрок"""
        while True:
            try:
                row_index = int(input("Выберете ряд, который заберете (1-4): ")) - 1
                if 0 <= row_index < len(table.rows):
                    print(f"Игрок {player.name}({player.score} выбрал ряд {row_index+1}")
                    return row_index
                else:
                    print("Повторите ввод. Введите число, указывающее на номер ряда ")
            except ValueError:
                print("Повторите ввод. Введите число, указывающее на номер ряда ")