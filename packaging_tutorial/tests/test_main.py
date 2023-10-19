<<<<<<< HEAD
import pytest

@pytest.mark.parameterize("test_input,expected", [(3,5,8), (2,4, 8)])

def test_eval(test_input1, test_input2, expected):
    assert(test_input1+test_input2 == expected)

>>>>>>> f4390da93d222dc3b6d3d736b41f739e1f01c373
