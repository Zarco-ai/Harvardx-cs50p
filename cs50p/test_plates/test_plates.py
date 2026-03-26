from plates import is_valid

# Test 1: Length (min 2, max 6)
def test_length():
    # Too short (Invalid)
    assert is_valid("A") == False
    assert is_valid("") == False
    # Too long (Invalid)
    assert is_valid("ABCDEF7") == False
    # Correct length (Valid)
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True

# Test 2: Starting Characters (must be letters)
def test_start_with_letters():
    # Must start with two letters (Invalid)
    assert is_valid("A2") == False
    assert is_valid("12") == False
    assert is_valid("A1BC") == False
    # Starts with two letters (Valid)
    assert is_valid("CS50") == True

# Test 3: No numbers in the middle (first number cannot be followed by a letter)
def test_numbers_in_middle():
    # Numbers in the middle (Invalid)
    assert is_valid("AAA22A") == False
    assert is_valid("A2BC") == False
    # Numbers at the end (Valid)
    assert is_valid("AAA222") == True
    assert is_valid("AAA2") == True

# Test 4: First number cannot be zero
def test_first_number_is_not_zero():
    # First number is 0 (Invalid)
    assert is_valid("CS05") == False
    assert is_valid("H01") == False
    # First number is not 0 (Valid)
    assert is_valid("CS50") == True
    assert is_valid("HI1") == True

# Test 5: No punctuation, spaces, or periods allowed
def test_punctuation():
    # Punctuation (Invalid)
    assert is_valid("PI3.14") == False
    assert is_valid("Hello!") == False
    assert is_valid("CS 50") == False
    # Only letters and numbers (Valid)
    assert is_valid("CS50") == True
    assert is_valid("ABC") == True
