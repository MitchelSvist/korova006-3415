from src.card import Card
from src.row import Row

row1 = [Card(3), Card(55), Card(70), Card(71), Card(72), Card(73)]

def test_init():
    r = Row()
    assert r.cards == []

def test_repr():
    r = Row()
    assert r.__repr__() == ''
    r.add_card(row1[0])
    assert r.__repr__() == '3'
    r.add_card(row1[1])
    assert r.__repr__() == '3 55'

def test_add_card():
    r = Row()
    r.add_card(row1[0])
    assert r.cards == [Card(3)]
    r.add_card(row1[1])
    assert r.cards == [Card(3), Card(55)]
    r.add_card(row1[2])
    assert r.cards == [Card(3), Card(55), Card(70)]

def test_has_max_lenght():
    r = Row()
    r.add_card(row1[0])
    assert r.has_max_length() == False
    r.add_card(row1[1])
    assert r.has_max_length() == False
    r.add_card(row1[2])
    assert r.has_max_length() == False
    r.add_card(row1[3])
    r.add_card(row1[4])
    r.add_card(row1[5])
    assert r.has_max_length() == True

def test_truncate():
    r = Row()
    r.add_card(row1[0])
    r.add_card(row1[1])
    assert r.truncate() == 8
    assert r.cards == []


def test_can_play_on():
    r = Row()
    assert r.can_play_on(row1[0])
    r.add_card(row1[1])
    assert not r.can_play_on(Card(54))
    assert r.can_play_on(Card(56))
    r.add_card(row1[2])
    assert not r.can_play_on(Card(1))
    assert r.can_play_on(Card(85))
