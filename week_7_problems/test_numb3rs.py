import numb3rs

def test_zeros():
    assert numb3rs.validate("001.1.01.1") == False
    assert numb3rs.validate("192.168.01.1") == False
    assert numb3rs.validate("102.120.0.10") == True

def test_valid():
    assert numb3rs.validate("") == False
    assert numb3rs.validate("   ") == False
    assert numb3rs.validate("0.0.0.0") == True

def test_numbers():
    assert numb3rs.validate("192.168.1.1") == True
    assert numb3rs.validate("192.168.256.1") == False
    assert numb3rs.validate("591.168.259.1") == False