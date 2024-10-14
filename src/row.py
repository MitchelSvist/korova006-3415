from src.card import Card

class Row:
    MAX_LEN_ROW = 6

    def __init__(self):
        self.cards: list[Card] = []

    def __repr__(self):
        return ' '.join(repr(card) for card in self.cards)

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