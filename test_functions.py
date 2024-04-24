import pytest
from functions import angle_between_hands

def test_angle_between_hands():
    assert angle_between_hands(12, 30) == 165
    assert angle_between_hands(3, 15) == 7.5
    assert angle_between_hands(6, 45) == 67.5
    assert angle_between_hands(9, 0) == 90
    assert angle_between_hands(11, 59) == 5.5

