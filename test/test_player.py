from src.hand import Hand
from src.player import Player


def test_init():
    h = Hand.load('55 5 95')
    p = Player(name='Mitchel', hand=h, score=11)
    assert p.name == 'Mitchel'
    assert p.hand == h
    assert p.score == 11

def test_str():
    h = Hand.load('55 5 95')
    p = Player(name='Mitchel', hand=h, score=11)
    assert str(p) == 'Mitchel(11): 55 5 95'

# def test_loser():
#     h = Hand.load('55 5 95')
#     p = Player(name='Mitchel', hand=h, score=65)
#     assert not p.loser()
#
#     p = Player(name='Mitchel', hand=h, score=66)
#     assert p.loser()


def test_eq():
    h1 = Hand.load('55 5 95')
    h2 = Hand.load('55 5 95')
    p1 = Player(name='Mitchel', hand=h1, score=11)
    p2 = Player(name='Mitchel', hand=h2, score=11)
    assert p1 == p2

def test_save():
    h = Hand.load('55 5 95')
    p = Player(name='Mitchel', hand=h, score=11)
    assert p.save() == {'name': 'Mitchel', 'score': 11, 'hand': '55 5 95'}

def test_load():
    data = {'name': 'Mitchel', 'score': 11, 'hand': '55 5 95'}
    h = Hand.load('55 5 95')
    p_expected = Player(name='Mitchel', hand=h, score=11)
    p = Player.load(data)
    assert p == p_expected