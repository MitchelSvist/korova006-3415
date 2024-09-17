class Card:
    NUMBERS = list(range(105))
    PENALTY_POINT = [1, 2, 3, 5, 7]

    def __init__(self, number: int, penalty_point: int):
        if number not in Card.NUMBERS:
            raise ValueError
        if penalty_point not in Card.PENALTY_POINT:
            raise ValueError
        self.number = number
        self.penalty_point = penalty_point

    def __repr__(self):
        return f'{self.number}_{self.penalty_point}'

    def __eq__(self, other):
        return self.number == other.number and self.penalty_point == other.penalty_point


    # def score(self) -> int:

    # def can_play_on(self, other) -> bool:
    #     """Можно ли играть карту self на карту other."""
    #     return self.color == other.color or self.number == other.number

    def save(self):
        return repr(self)

    def load(text: str):
        """From 'y3' to Card('y', 3)."""
        text = text.split("_")
        return Card(number=int(text[0]), penalty_point=int(text[1]))
