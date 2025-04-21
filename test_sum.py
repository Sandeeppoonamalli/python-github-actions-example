# test_sum.py
from sum import add_numbers, subtract_numbers

# Test addition
def test_add_numbers():
    assert add_numbers(5, 10) == 15  # Test case for the sum of 5 and 10
    assert add_numbers(0, 0) == 0    # Test case for the sum of 0 and 0
    assert add_numbers(-1, 1) == 0   # Test case for the sum of -1 and 1

# Test subtraction
def test_subtract_numbers():
    assert subtract_numbers(10, 5) == 5   # Test case for 10 - 5
    assert subtract_numbers(0, 0) == 0    # Test case for 0 - 0
    assert subtract_numbers(1, -1) == 2   # Test case for 1 - (-1)
