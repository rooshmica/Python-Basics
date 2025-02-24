def square(number):
    return number * number

# this is the test function
def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-5) == 25

# On the command-line, run the command: pytest test_square_function.py


