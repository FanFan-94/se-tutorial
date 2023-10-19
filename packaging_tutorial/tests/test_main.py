import pytest

@pytest.mark.parametrize("test_input,expected", [(3,4), (4,8)])
def test_main(test_input1, expected):
    assert(test_input1+1 == expected)

