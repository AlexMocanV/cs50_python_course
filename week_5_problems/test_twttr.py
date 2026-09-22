from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "hll"
    assert shorten("hElLo") == "hll"
    assert shorten("Hello") == "hll"
    assert shorten("aeiou") == ""

