import pytest

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import multiply_by_ten

def test_multiply_by_ten_int():
    assert multiply_by_ten("5") == 50

def test_multiply_by_ten_float():
    assert multiply_by_ten("3.5") == 35.0

def test_multiply_by_ten_invalid_input():
    with pytest.raises(ValueError):
        multiply_by_ten("not a number")

def test_multiply_by_ten_non_number():
    with pytest.raises(ValueError):
        multiply_by_ten("[1, 2, 3]")