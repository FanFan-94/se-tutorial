import pytest
@pytest.mark.parametrize("test_input,expected", [(3,5,8), (2,4,8)])
def test_main(test_input1, test_input2, expected):
    assert(test_input1+test_input2 == expected)

