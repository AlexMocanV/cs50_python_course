import pytest
import working

def test_convert():
    assert working.convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert working.convert("12:15 PM to 12:45 AM") == "12:15 to 00:45"
    assert working.convert("1:15 PM to 11:45 PM") == "13:15 to 23:45"
    assert working.convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert working.convert("11:15 AM to 1:45 PM") == "11:15 to 13:45"

def test_invalid_time():
    with pytest.raises(ValueError):
        working.convert("25 AM to 5 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM to 60 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM to 5:60 PM")
    with pytest.raises(ValueError):
        working.convert("9:89 AM to 5 PM")
    with pytest.raises(ValueError):
        working.convert("9 AM5 PM") 