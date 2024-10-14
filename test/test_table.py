from src.card import Card
from src.row import Row
from src.table import Table


def test_table_init():
    table = Table()
    assert len(table.rows) == 4
    assert (isinstance(row, Row) for row in table.rows)


