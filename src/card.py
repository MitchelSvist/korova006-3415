class Card:
    NUMBERS = list(range(105))

    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError
        self.number = number

    def __repr__(self):
        return f'{self.number}'

    def __eq__(self, other):
        return self.number == other.number

    def score(self) -> int:
        if self.number == 55:
            return 7
        elif self.number % 11 == 0:
            return 5
        elif self.number % 10 == 0:
            return 3
        elif self.number % 5 == 0:
            return 2
        else:
            return 1

    def can_play_on(self, other) -> bool:
        """Можно ли играть карту self на карту other."""
        return self.number < other.number

    def save(self):
        return repr(self)

    def load(text: str):
        return Card(number=int(text))
