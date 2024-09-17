from src.card import Card

def test_init():
    c = Card(55, 7)
    assert c.number == 55
    assert c.penalty_point == 7

# def test_play_on():
#     c1 = Card.load('y1')
#     c2 = Card.load('y5')
#     c3 = Card.load('g1')
#     c4 = Card.load('g6')
#
#     assert c1.can_play_on(c1)
#     assert c2.can_play_on(c1)
#     assert c1.can_play_on(c2)
#     assert c3.can_play_on(c1)
#     assert not c4.can_play_on(c1)

def test_save():
    c = Card(30, 3)
    assert repr(c) == "30_3"
    assert c.save() == "30_3"

    c = Card(55, 7)
    assert repr(c) == "55_7"
    assert c.save() == "55_7"

def test_load():
    s = "20_3"
    c = Card.load(s)
    assert c == Card(20, 3)
    s = "5_1"
    c = Card.load(s)
    assert c == Card(5, 1)