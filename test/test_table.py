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

    table.add_card(Card(10))
    table.add_card(Card(25))
    table.add_card(Card(50))
    table.add_card(Card(60))
    table.add_card(Card(55))
    table.add_card(Card(62))
    table.add_card(Card(67))


    expected_repr = f"r1: {Card(10)}\nr2: {Card(25)}\nr3: {Card(50)} {Card(55)}\nr4: {Card(60)} {Card(62)} {Card(67)}"
    assert repr(table) == expected_repr



def test_add_card():
    table = Table()

    # Добавление карт
    table.add_card(Card(10))
    table.add_card(Card(25))
    table.add_card(Card(50))
    table.add_card(Card(60))
    table.add_card(Card(55))
    table.add_card(Card(62))
    table.add_card(Card(67))
    table.add_card(Card(83))
    table.add_card(Card(100))

    assert repr(table[0]) == '10'
    assert repr(table[1]) == '25'
    assert repr(table[2]) == '50 55'
    assert repr(table[3]) == '60 62 67 83 100'
    assert not table.add_card(Card(1)) #нет подходящего ряда
    assert not table.add_card(Card(9)) #нет подходящего ряда



def test_save_load():
    """Сохранение и загрузку стола."""
    table = Table()
    table.add_card(Card(10))
    table.add_card(Card(25))
    table.add_card(Card(50))
    table.add_card(Card(60))
    table.add_card(Card(55))
    table.add_card(Card(62))
    table.add_card(Card(67))
    table.add_card(Card(83))
    table.add_card(Card(100))

    row = Row()
    row.add_card(Card(50))
    row.add_card(Card(55))

    saved_data = table.save()
    loaded_data = json.loads(saved_data)
    new_table = Table.load(loaded_data)

    assert new_table[0].cards[0] == Card(10)

    assert new_table[1].cards[0] == Card(25)

    assert new_table[2].cards[0] == Card(50)
    assert new_table[2].cards[1] == Card(55)
    assert new_table[2] == row


    assert len(new_table[0].cards) == 1
    assert len(new_table[1].cards) == 1
    assert len(new_table[2].cards) == 2
    assert len(new_table[3].cards) == 5