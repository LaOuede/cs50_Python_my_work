from bank import value


def test_value_numeric():
    assert value("123") == 100
    assert value("salut123") == 100
    assert value("-124Hey") == 100


def test_value_upper():
    assert value("HHEY") == 20
    assert value("HHELLO") == 20
    assert value("SALUT") == 100


def test_value_lower():
    assert value("ola") == 100
    assert value("bonjour merci") == 100
    assert value("what's happening") == 100


def test_value_good():
    assert value("Hello") == 0
    assert value("Hello, world") == 0
    assert value("Hello salut") == 0
