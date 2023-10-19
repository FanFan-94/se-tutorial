import pytest
<<<<<<< HEAD
from add import add_value
=======

>>>>>>> f16bd2b75a7e7e00db02d7a1885a9fab7c4407f7
@pytest.mark.parametrize("test_input,expected", [(3,4), (4,5)])
def test_main(test_input, expected):
    assert(add_value(test_input) == expected)

