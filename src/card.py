class Card:
    NUMBERS = list(range(1, 105))

    def __init__(self, number: int):
        if number not in Card.NUMBERS:
            raise ValueError
        self.number = number

    def __repr__(self):
        return f'{self.number}'

    def __eq__(self, other):
        return self.number == other.number

    def penalty_score(self) -> int:
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

    def can_place_after(new_card, last_card) -> bool:
        """Можно ли играть карту new_card на карту last_card."""
        return new_card.number > last_card.number

    def all_cards(numbers: None | list[int] = None):
        if numbers is None:
            numbers = Card.NUMBERS
        cards = [Card(number=num) for num in numbers]
        return cards

    def save(self):
        return repr(self)

    @staticmethod
    def load(text: str):
        return Card(number=int(text))
