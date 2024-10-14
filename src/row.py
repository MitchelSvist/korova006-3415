from src.card import Card

class Row:

    def __init__(self):
        self.cards: list[Card] = []

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)

    def add_card(self, card: Card):
        self.cards.append(card)

    def has_max_length(self) -> bool:
        return len(self.cards) >= 6

    def truncate(self):
        self.cards.clear()