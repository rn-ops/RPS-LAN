import pytest
from common.modes import OneVsOne, FreeForAll


def test_one_vs_one_valid():
    mode = OneVsOne()
    moves = {"p1": "rock", "p2": "scissors"}
    result = mode.play_round(moves)
    assert result == {"p1": "win", "p2": "lose"}


def test_one_vs_one_invalid_player_count():
    mode = OneVsOne()
    moves = {"p1": "rock"}
    with pytest.raises(ValueError):
        mode.play_round(moves)


def test_free_for_all_all_same():
    mode = FreeForAll()
    moves = {"p1": "rock", "p2": "rock", "p3": "rock"}
    result = mode.play_round(moves)
    assert all(v == "draw" for v in result.values())


def test_free_for_all_all_three_moves():
    mode = FreeForAll()
    moves = {"p1": "rock", "p2": "paper", "p3": "scissors"}
    result = mode.play_round(moves)
    assert all(v == "draw" for v in result.values())


def test_free_for_all_two_moves_one_wins():
    mode = FreeForAll()
    moves = {"p1": "rock", "p2": "rock", "p3": "scissors"}
    result = mode.play_round(moves)
    assert result["p1"] == "win"
    assert result["p2"] == "win"
    assert result["p3"] == "lose"


def test_free_for_all_two_moves_other_wins():
    mode = FreeForAll()
    moves = {"p1": "rock", "p2": "paper", "p3": "paper"}
    result = mode.play_round(moves)
    assert result["p1"] == "lose"
    assert result["p2"] == "win"
    assert result["p3"] == "win"
