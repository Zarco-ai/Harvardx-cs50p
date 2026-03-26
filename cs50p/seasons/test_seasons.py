from seasons import how_old
from datetime import date
import pytest

def test_how_old_one_year():
    # Test exactly 365 days ago
    # 365 days * 24 hours * 60 minutes = 525600
    today = date(2020, 1, 1)
    birth = date(2019, 1, 1)
    assert how_old(today, birth) == 525600

def test_how_old_two_years():
    # Test exactly 730 days ago
    # 730 days * 1440 minutes = 1051200
    today = date(2020, 1, 1)
    birth = date(2018, 1, 1)
    assert how_old(today, birth) == 1051200

# Optional: Test for a leap year
def test_leap_year():
    # 2020 was a leap year (366 days)
    # 366 * 1440 = 527040
    today = date(2021, 1, 1)
    birth = date(2020, 1, 1)
    assert how_old(today, birth) == 527040
