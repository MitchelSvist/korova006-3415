import json
from src.card import Card
from src.row import Row


class Table:
    def __init__(self):
        self.rows: list[Row] = [Row() for _ in range(4)]

    def __repr__(self):
        repr_rows = [f"row{i + 1}: {repr(row)}" for i, row in enumerate(self.rows)]
        return "\n".join(repr_rows)

    def __getitem__(self, item) -> Row:
        return self.rows[item]

    def add_card(self, card: Card) -> bool:
        acceptable_rows = []
        for row in self.rows:
            if row.can_play_on(card):
                acceptable_rows.append(row)

        if not acceptable_rows:
            return False

        # for row in acceptable_rows:
        #     if len(f'{row}')==0: #как изменить?????????????????
        #         row.add_card(card)
        #         return True

        best_row = min(acceptable_rows, key=lambda r: abs(card.number - r.cards[-1].number))
        best_row.add_card(card)
        return True

    def save(self) -> str:
        return json.dumps({f"row{i + 1}": self.rows[i].save() for i in range(len(self.rows))})

    @classmethod
    def load(cls, rows_data: dict):
        table = cls()
        for row_key, cards_str in rows_data.items():
            table.rows[int(row_key[-1])-1] = Row.load(cards_str)
        return table