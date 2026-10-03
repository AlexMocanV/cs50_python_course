import um

def test_count():
    assert um.count("u_m") == 0
    assert um.count("Um") == 1
    assert um.count("UM") == 1
    assert um.count("um, (um, um") == 3
    assert um.count("um, Um}, UM") == 3
    assert um.count("um, {}Um{}, UM, uM, UuMm") == 4
    assert um.count("um, Um, _UM, uM, UuMm, UuMm") == 3