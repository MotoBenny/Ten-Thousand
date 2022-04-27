import pytest
from ten_thousand.game_logic import GameLogic



def test_single_five(): # Covered
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected


def test_single_one(): # covered
    actual = GameLogic.calculate_score((1,))
    expected = 100
    assert actual == expected


def test_two_fives(): # Covered
    actual = GameLogic.calculate_score((5, 5))
    expected = 100
    assert actual == expected


def test_this_weird_roll(): # covered
    actual = GameLogic.calculate_score((3, 6, 3, 2, 4, 2))
    expected = 0
    assert actual == expected


def test_two_ones(): # covered
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected


def test_one_and_five(): # Covered
    actual = GameLogic.calculate_score((5, 1))
    expected = 150
    assert actual == expected


def test_zilch(): # Covered
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected


def test_three_fives(): # Failing
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected


def test_three_ones(): # Failing
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five(): # Failing
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


def test_straight(): # Covered
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    expected = 1500
    assert actual == expected


def test_three_of_a_kind(): # covered
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected


def test_four_of_a_kind(): # covered
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected


def test_five_of_a_kind(): # covered
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    expected = 600
    assert actual == expected


def test_six_of_a_kind(): # covered
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected


def test_six_ones(): # covered
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    expected = 4000
    assert actual == expected


def test_two_twos_two_threes_and_two_sixs_scores_the_user_1500_points(): # covered
    actual = GameLogic.calculate_score((2, 3, 6, 2, 3, 6))
    expected = 1500
    assert actual == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100), # COVERED
        ((1, 1), 200), # covered
        ((1, 1, 1), 1000),  # covered
        ((1, 1, 1, 1), 2000),  # covered
        ((1, 1, 1, 1, 1), 3000), # covered
        ((1, 1, 1, 1, 1, 1), 4000), # covered
        ((2,), 0), # covered
        ((2, 2), 0), # covered
        ((2, 2, 2), 200), # covered
        ((2, 2, 2, 2), 400),  # covered
        ((2, 2, 2, 2, 2), 600), # covered
        ((2, 2, 2, 2, 2, 2), 800), # covered
        ((3,), 0), # covered
        ((3, 3), 0), # covered
        ((3, 3, 3), 300), # covered
        ((3, 3, 3, 3), 600),  # covered
        ((3, 3, 3, 3, 3), 900), # covered
        ((3, 3, 3, 3, 3, 3), 1200), # covered
        ((4,), 0), # covered
        ((4, 4), 0), # covered
        ((4, 4, 4), 400), # covered
        ((4, 4, 4, 4), 800),  # covered
        ((4, 4, 4, 4, 4), 1200), # covered
        ((4, 4, 4, 4, 4, 4), 1600), # covered
        ((5,), 50), # covered
        ((5, 5), 100), # covered
        ((5, 5, 5), 500), # covered
        ((5, 5, 5, 5), 1000),  # covered
        ((5, 5, 5, 5, 5), 1500), # covered
        ((5, 5, 5, 5, 5, 5), 2000), # covered
        ((6,), 0), # covered
        ((6, 6), 0), # covered
        ((6, 6, 6), 600), # covered
        ((6, 6, 6, 6), 1200),  # covered
        ((6, 6, 6, 6, 6), 1800), # covered
        ((6, 6, 6, 6, 6, 6), 2400), # covered
        ((1, 2, 3, 4, 5, 6), 1500), # covered
        ((2, 2, 3, 3, 4, 6), 0), # Covered
        ((2, 2, 3, 3, 6, 6), 1500), # covered
        ((1, 1, 1, 2, 2, 2), 1200), # covered
    ],
)
def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected