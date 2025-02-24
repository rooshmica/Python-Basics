
from metric_calculations import convert_to_imperial, convert_to_metres

# these are the test functions
def test_convert_to_imperial():
    assert convert_to_imperial(8.9) == 2.393712000000008

def test_convert_to_imperial():
    assert convert_to_metres(6,2.5) == 1.8923

# To use this, the file needs to be renamed as test_metric_functions.py
# On the command-line, run the command: pytest test_metric_functions.py

