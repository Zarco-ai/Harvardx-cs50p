from bank import value

def test_value():
    # TEST CASES FOR $0
    # Basic
    assert value("Hello") == "$0"
    # Case-insensitive
    assert value("HELLO") == "$0"
    # Leading/Trailing Whitespace
    assert value("  hello ") == "$0"
    # Full phrase
    assert value("Hello, World!") == "$0"

    # TEST CASES FOR $20
    # Basic
    assert value("h") == "$20"
    assert value("Hi") == "$20"
    # Case-insensitive
    assert value("HEY") == "$20"
    # Leading/Trailing Whitespace
    assert value("  Howdy ") == "$20"
    # Full phrase
    assert value("How are you?") == "$20"

    # TEST CASES FOR $100
    # Basic
    assert value("What's up?") == "$100"
    assert value("Goodbye") == "$100"
    # Leading/Trailing Whitespace
    assert value("  Welcome ") == "$100"
