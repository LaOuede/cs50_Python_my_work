from plates import is_valid

def test_length():
    assert is_valid('ABGT635') == False
    assert is_valid('A') == False
    assert is_valid('AI') == True
    assert is_valid('AGT654') == True


def test_2letters():
    assert is_valid('1AGFTR') == False
    assert is_valid('12GTFE') == False
    assert is_valid('A2GTFE') == False
    assert is_valid('ABC123') == True
    assert is_valid('GF') == True
    assert is_valid('G8') == False


def test_alnum():
    assert is_valid('AHT/12') == False
    assert is_valid('AGD8-6') == False
    assert is_valid('AB 635') == False
    assert is_valid('1.SR') == False


def test_digits():
    assert is_valid('12SR35') == False
    assert is_valid('134RAS') == False
    assert is_valid('ABC123') == True
    assert is_valid("AB12C") == False
    assert is_valid('R1AS') == False
    assert is_valid('AB35') == True
    assert is_valid('1Q') == False
    assert is_valid('AB') == True


def test_zero():
    assert is_valid('ABR035') == False

