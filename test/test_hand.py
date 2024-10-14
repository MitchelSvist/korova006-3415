from src.card import Card
from src.hand import Hand

cards = [Card(3), Card(70), Card(55), Card(5), Card(104)]


def test_init():
    h = Hand(cards=cards)
    assert h.cards == cards


def test_repr():
    h = Hand(cards)
    h1 = Hand([Card(9)])

    assert h.__repr__() == '3 70 55 5 104'
    assert h1.__repr__() == '9'
    assert Hand([Card(4)]).__repr__() == '4'


def test_eq():
    h = Hand(cards)
    h1 = Hand(cards)
    h2 = Hand([Card(3), Card(70), Card(55), Card(5), Card(104)])
    h3 = Hand([Card(40), Card(51)])

    assert h == h1
    assert h == h2
    assert h != h3


def test_add_card():
    h = Hand.load('3 70 55 5 104')
    h.add_card(Card.load('60'))
    assert repr(h) == '3 70 55 5 104 60'

    h.add_card(Card.load('66'))
    assert repr(h) == '3 70 55 5 104 60 66'

    h.add_card(Card(34))
    assert repr(h) == '3 70 55 5 104 60 66 34'


def test_save():
    h = Hand(cards=cards)
    assert h.save() == '3 70 55 5 104'

    h = Hand(cards=[])
    assert h.save() == ''


def test_load():
    h = Hand.load('3 70 55 5 104')
    expected_deck = Hand(cards)
    assert h == expected_deck


def test_score():
    h = Hand.load('3 70 55 5 104')
    assert h.score() == 14

    h = Hand.load('3 70 5 104')
    assert h.score() == 7


def test_remove_card():
    h = Hand.load('3 70 55 5 104')
    c = Card.load('70')
    h.remove_card(c)
    assert repr(h) == '3 55 5 104'