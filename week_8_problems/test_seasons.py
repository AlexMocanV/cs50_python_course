import pytest
from seasons import convert_to_words, get_difference, validate_input 
from datetime import date

def test_validate_input():
    assert(validate_input("1999-01-01")) == True
    assert(validate_input("1999-08-29")) == True
    assert(validate_input("1999-02-30")) == False 
    assert(validate_input("2024-02-29")) == True

def test_get_difference():
    assert get_difference("1999-01-01", date(2000, 1, 1)) == 525600

def test_convert_to_words():
    assert(convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes")