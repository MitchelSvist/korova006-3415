import json
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def __repr__(self):
        repr_rows = [f"row{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)

    def __str__(self):
        str_rows = [f"row{i + 1}: {str(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(str_rows)

    def __getitem__(self, item) -> Row:
        return self.rows[item]

    # def add_card(self, card: Card) -> bool:
    #     acceptable_rows = []
    #     for row in self.rows:
    #         if row.can_play_on(card):
    #             acceptable_rows.append(row)
    #
    #     if not acceptable_rows:
    #         return False
    #
    #     best_row = min(acceptable_rows, key=lambda r: abs(card.number - r.cards[-1].number))
    #     # if best_row.has_max_length():
    #
    #     best_row.add_card(card)
    #     return True

    def add_card(self, card: Card) -> (bool, Row):
        acceptable_rows = []
        for row in self.rows:
            if row.can_play_on(card):
                acceptable_rows.append(row)

        if not acceptable_rows:
            return False, None

        best_row = min(acceptable_rows, key=lambda r: abs(card.number - r.cards[-1].number))

        if best_row.has_max_length():
            return False, best_row

        best_row.add_card(card)
        return True, best_row

    def save(self) -> str:
        return json.dumps({f"row{i + 1}": self.rows[i].save() for i in range(len(self.rows))})

    @classmethod
    def load(cls, rows_data: dict):
        table = cls()
        for row_key, cards_str in rows_data.items():
            table.rows[int(row_key[-1])-1] = Row.load(cards_str)
        return table