from src.card import Card

def test_init():
    c = Card(55)
    assert c.number == 55

def test_repr():
    c = Card(55)
    assert c.__repr__() == '55'
    assert Card.__repr__(Card(60)) == '60'

def test_eq():
    a = Card(10)
    c = Card(78)
    b = Card(78)
    d = Card(78)

    assert c == b
    assert c == d
    assert c == Card(78)
    assert c != a
    assert c != Card(11)

def test_score():
    c = Card(70)
    assert 3 == c.score()
    c = Card(55)
    assert 7 == c.score()
    c = Card(11)
    assert 5 == c.score()

def test_play_on():
    c1 = Card.load('1')
    c2 = Card.load('55')
    c3 = Card.load('11')
    c4 = Card.load('104')

    assert not c1.can_play_on(c1)
    assert not c2.can_play_on(c1)
    assert c1.can_play_on(c2)
    assert not c3.can_play_on(c1)
    assert c1.can_play_on(c4)

def test_save():
    c = Card(30)
    assert repr(c) == "30"
    assert c.save() == "30"

    c = Card(55)
    assert repr(c) == "55"
    assert c.save() == "55"

def test_load():
    s = "20"
    c = Card.load(s)
    assert c == Card(20)
    s = "5"
    c = Card.load(s)
    assert c == Card(5)
