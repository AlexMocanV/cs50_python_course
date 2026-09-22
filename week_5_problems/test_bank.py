from bank import value 

def test_lowercase():
    assert value(["hello"]) == 0
    assert value(["hey"]) == 20
def test_uppercase():    
    assert value(["Hi"]) == 20
    assert value(["Hello"]) == 0
def test_other():
    assert value(["What's up?"]) == 100
    assert value([""]) == 100