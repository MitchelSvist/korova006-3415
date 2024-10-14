import json
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def add_card(self, card: Card) -> bool:
        pass

    def choose_row(self, index_row: int) -> Row:
        return self.rows[index_row]

    def min_card(self):
        return min(r[-1] for r in self.rows)