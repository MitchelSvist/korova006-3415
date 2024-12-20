from src.card import Card

class Row:
    MAX_LEN_ROW = 5

    def __init__(self):
        self.cards: list[Card] = []

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)

    def __str__(self):
        return ' '.join(repr(card)+f"({card.penalty_score()})" for card in self.cards)

    def __eq__(self, other):
        return self.cards == other.cards

    def add_card(self, card: Card):
        self.cards.append(card)

    def has_max_length(self) -> bool:
        return len(self.cards) >= self.MAX_LEN_ROW

    def truncate(self) -> int:
        sum_point = sum(c.penalty_score() for c in self.cards)
        self.cards.clear()
        return sum_point

    def can_play_on(self, card: Card) -> bool:
        return not self.cards or card.can_place_after(self.cards[-1])

    def save(self) -> str:
        return ' '.join(card.save() for card in self.cards)

    @staticmethod
    def load(data: str) -> 'Row':
        row = Row()
        list_cards = data.split(' ')
        for card in list_cards:
            row.add_card(Card.load(card))
        return row