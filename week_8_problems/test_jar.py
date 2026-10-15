import jar
import pytest

def test_init():
    jarr = jar.get_jar(5)
    jarr.deposit(3)
    return jarr

def test_deposit():
    jarr = test_init()
    assert (jarr.size == 3) 
    jarr.withdraw(2)
    assert (jarr.size == 1)
    with pytest.raises(ValueError):
        jarr.withdraw(2)
    with pytest.raises(ValueError):
        jarr.deposit(6)    


def test_withdraw():
    jarr = test_init()
    assert (jarr.size == 3) 
    jarr.withdraw(2)
    assert (jarr.size == 1)
    with pytest.raises(ValueError):
        jarr.withdraw(2)
    with pytest.raises(ValueError):
        jarr.deposit(6)    

def test_str():
    jarr = jar.get_jar(7)
    assert(str(jarr) == "")
    jarr.deposit(6)
    assert(str(jarr) == "🍪🍪🍪🍪🍪🍪")
    jarr.withdraw(4)
    assert(str(jarr) == "🍪🍪")
    
