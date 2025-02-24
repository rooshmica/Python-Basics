from metric_calculations import convert_to_imperial, convert_to_metres

# import the approx function from pytest
from pytest import approx

# these are the test functions
def test_convert_to_imperial():
    assert convert_to_imperial(8.9) == (29,approx(2.4, 0.1))

def test_convert_to_metres():
    assert convert_to_metres(6,2.5) == approx(1.89, 0.1)

# On the command-line, run the command: pytest test_metric_functions.py

