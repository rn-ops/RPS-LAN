import pytest
from common.game_logic import beats, decide_winner_basic


def test_beats():
    assert beats("rock", "scissors")
    assert beats("scissors", "paper")
    assert beats("paper", "rock")
    assert not beats("rock", "paper")
    assert not beats("scissors", "rock")
    assert not beats("paper", "scissors")


def test_decide_winner_basic_draw():
    moves = {"p1": "rock", "p2": "rock"}
    result = decide_winner_basic(moves)
    assert result == {"p1": "draw", "p2": "draw"}


def test_decide_winner_basic_p1_wins():
    moves = {"p1": "rock", "p2": "scissors"}
    result = decide_winner_basic(moves)
    assert result == {"p1": "win", "p2": "lose"}


def test_decide_winner_basic_p2_wins():
    moves = {"p1": "scissors", "p2": "rock"}
    result = decide_winner_basic(moves)
    assert result == {"p1": "lose", "p2": "win"}
