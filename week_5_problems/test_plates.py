from plates import is_valid

def test_first_two():
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("AB") == True
def test_length():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEFG") == False
def test_last():
    assert is_valid("AB1") == True
    assert is_valid("AB0F") == False
    assert is_valid("AB1C") == False
def test_zero():
    assert is_valid("AB01") == False
    assert is_valid("AB10") == True
def test_punctuation():
    assert is_valid("AB!") == False
    assert is_valid("AB@") == False
    assert is_valid("AB.") == False
    assert is_valid("AB ") == False