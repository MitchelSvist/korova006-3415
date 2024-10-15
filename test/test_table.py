import json
from src.card import Card
from src.row import Row
from src.table import Table


def test_table_init():
    table = Table()
    assert len(table.rows) == 4
    assert (isinstance(row, Row) for row in table.rows)

def test_repr():
    table = Table()

    table.add_card(Card(10), 0)
    table.add_card(Card(40), 0)
    table.add_card(Card(9), 0)
    table.add_card(Card(9), 1)

    expected_repr = f"r1: {Card(10)} {Card(40)}\nr2: {Card(9)}\nr3: \nr4: "
    assert repr(table) == expected_repr

def test_choose_row():
    table = Table()
    row = Row()

    table.add_card(Card(10), 0)
    table.add_card(Card(25), 0)
    row.add_card(Card(10))
    row.add_card(Card(25))

    assert table.choose_row(0) == row

def test_add_card():
    table = Table()

    assert table.add_card(Card(10), 0)
    assert table.add_card(Card(11), 0)
    assert table.add_card(Card(55), 1)
    assert not table.add_card(Card(54), 1)
    assert table.add_card(Card(56), 1)
    assert table.add_card(Card(54), 3)
    assert table.add_card(Card(99), 3)

# def test_min_card():
#     table = Table()
#     table.add_card(Card(10), 0)
#     table.add_card(Card(25), 1)
#     table.add_card(Card(11), 2)
#     table.add_card(Card(9), 2)
#     table.add_card(Card(12), 2)
#     assert table.min_card() == Card(10)

def test_save_load():
    """Сохранение и загрузку стола."""
    table = Table()
    table.add_card(Card(10), 0)
    table.add_card(Card(25), 1)
    table.add_card(Card(11), 2)
    table.add_card(Card(9), 2)
    table.add_card(Card(12), 2)
    row = Row()
    row.add_card(Card(11))
    row.add_card(Card(12))

    saved_data = table.save()
    loaded_data = json.loads(saved_data)
    new_table = Table.load(loaded_data)

    assert new_table[0].cards[0] == Card(10)

    assert new_table[1].cards[0] == Card(25)

    assert new_table[2].cards[0] == Card(11)
    assert new_table[2].cards[1] == Card(12)
    assert new_table[2] == row


    assert len(new_table[0].cards) == 1
    assert len(new_table[1].cards) == 1
    assert len(new_table[2].cards) == 2