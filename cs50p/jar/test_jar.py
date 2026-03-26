import pytest
from jar import Jar

def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    # Test default capacity
    default_jar = Jar()
    assert default_jar.capacity == 12
    # Test invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("cat")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    # Test depositing over capacity
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
    # Test withdrawing more than available
    with pytest.raises(ValueError):
        jar.withdraw(1)
