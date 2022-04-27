import pytest
from ten_thousand.game_logic import GameLogic


@pytest.mark.skip("passing")
def test_validate_legal_keepers():
    roll = (1, 2, 3, 4, 5)
    keepers = (5, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = True
    assert actual == expected


@pytest.mark.skip("passing")
def test_validate_illegal_keepers():
    roll = (1, 2, 3, 4, 5)
    keepers = (1, 1, 1, 1, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected


@pytest.mark.skip("passing")
def test_validate_illegal_overflow():
    roll = (1,)
    keepers = (1, 1, 1, 1, 1, 1)
    actual = GameLogic.validate_keepers(roll, keepers)
    expected = False
    assert actual == expected