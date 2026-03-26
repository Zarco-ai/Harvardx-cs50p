from um import count

def test_basic():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_substrings():
    assert count("yummy") == 0
    assert count("instrument") == 0

def test_case_sensitivity():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
