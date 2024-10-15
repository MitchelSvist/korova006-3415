import json
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def __repr__(self):
        repr_rows = [f"r{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)

    def __getitem__(self, item):
        return self.rows[item]

    def add_card(self, card: Card, index_row: int) -> bool:
        if self.rows[index_row].can_play_on(card):
            self.rows[index_row].add_card(card)
            return True

    def choose_row(self, index_row: int) -> Row:
        return self.rows[index_row]

    # def min_card(self):
        # return min(r[-1] for r in self.rows)

    def save(self) -> str:
        return json.dumps([[card.number for card in row.cards] for row in self.rows])

    @classmethod
    def load(cls, rows_data: list):
        table = cls()
        for row_index, cards in enumerate(rows_data):
            for card_data in cards:
                card = Card.load(f'{card_data}')
                table.add_card(card, row_index)
        return table