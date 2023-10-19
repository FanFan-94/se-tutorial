import pytest

from packaging_tutorial.add import add_value
@pytest.mark.parametrize("test_input,expected", [(3,4), (4,5)])
def test_main(test_input, expected):
    assert(add_value(test_input) == expected)

