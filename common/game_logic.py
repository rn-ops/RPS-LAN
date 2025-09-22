BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

def beats(move1, move2):
    """
    Return True if move1 beats move2, else False.
    """
    return BEATS[move1] == move2


def decide_winner_basic(moves):
    """
    Decide winner in 1v1 mode.
    moves: dict {player_id: "rock"/"paper"/"scissors"}
    returns: dict {player_id: "win"/"lose"/"draw"}
    """
    (p1, m1), (p2, m2) = moves.items()
    return (
        {p1: "draw", p2: "draw"} if m1 == m2
        else {p1: "win", p2: "lose"} if beats(m1, m2)
        else {p1: "lose", p2: "win"}
    )