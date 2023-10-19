import pytest

@pytest.mark.parametrize("test_input,expected", [(3,4), (4,8)])
def test_main(test_input, expected):
    assert(test_input+1 == expected)

