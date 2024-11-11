import random

from src.card import Card
from src.deck import Deck

cards = [Card(3), Card(70), Card(55), Card(5), Card(104)]

def test_init():
    d = Deck(cards=cards)
    assert d.cards == cards


def test_init_shuffle():
    """Проверяем, что карты в другом порядке."""
    full_deck1 = Deck(None)
    full_deck2 = Deck(None)
    assert len(full_deck1.cards) == len(full_deck2.cards)
    assert full_deck1.cards != full_deck2.cards

def test_repr():
    d = Deck(cards)
    d1 = Deck([Card(9)])

    assert repr(d) == "3 70 55 5 104"
    assert repr(d1) == "9"
    assert repr(Deck([Card(4)])) == "4"


def test_eq():
    d = Deck(cards)
    d1 = Deck(cards)
    d2 = Deck([Card(3), Card(70), Card(55), Card(5), Card(104)])
    d3 = Deck([Card(40), Card(51)])

    assert d == d1
    assert d == d2
    assert d != d3

def test_draw_card():
    d1 = Deck.load('3 30 77')
    d2 = Deck.load('3 30')
    c = d1.draw_card()
    assert c == Card.load('77')
    assert d1 == d2

def test_shuffle():
    random.seed(3)
    deck = Deck(cards=cards)

    deck.shuffle()
    assert deck.save() == '3 55 5 104 70'

    deck.shuffle()
    assert deck.save() == '55 104 5 3 70'

    deck.shuffle()
    assert deck.save() == '104 55 70 5 3'

def test_save():
    d = Deck(cards=cards)
    assert d.save() == '3 70 55 5 104'

    d = Deck(cards=[])
    assert d.save() == ''

def test_load():
    d = Deck.load("3 70 55 5 104")
    expected_deck = Deck(cards)
    assert d == expected_deck



