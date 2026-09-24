from twttr import shorten


def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hElLo") == "hLl"
    assert shorten("Hello") == "Hll"
    assert shorten("aeiouAEIOU") == ""

    
    assert shorten("cs50 2026") == "cs50 2026"
    assert shorten("hello, world!") == "hll, wrld!"