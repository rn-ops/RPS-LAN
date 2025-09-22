from common.game_logic import decide_winner_basic


class BaseMode:
    """Abstract base for all game modes."""

    def play_round(self, moves, **kwargs):
        """
        moves: dict {player_id: "rock"/"paper"/"scissors"}
        returns: dict {player_id: "win"/"lose"/"draw"}
        """
        raise NotImplementedError("This method should be overridden by subclasses.")


class OneVsOne(BaseMode):
    """Classic 2-player Rock Paper Scissors."""

    def play_round(self, moves, **kwargs):
        if len(moves) != 2:
            raise ValueError("1v1 mode requires exactly 2 players.")
        return decide_winner_basic(moves)



'''
Start FFA
Number of players -> X
active_players = [all players]

while len(active_players) > 1:
    moves = get_moves(active_players)
    outcome = decide_round_winner(moves)  # returns win/lose/draw
    active_players = [players who won this round]
    
Declare winner(s) or draw
'''
class FreeForAll(BaseMode):
    """Multi-round Free-for-All with elimination until one winner remains."""

    def play_round(self, moves_dict):
        """
        moves_dict: dict {player_id: move}
        Returns: dict {player_id: "win"/"lose"/"draw"}
        """
        active_players = list(moves_dict.keys())
        player_moves = moves_dict.copy()  # initial moves

        round_num = 1
        while len(active_players) > 1:
            # Collect current round moves
            current_moves = {p: player_moves[p] for p in active_players}
            unique_moves = set(current_moves.values())

            print(f"\n--- Round {round_num} ---")
            for p in active_players:
                print(f"{p}: {current_moves[p]}")

            # Draw conditions
            if len(unique_moves) == 1:
                print("All players chose the same. Round is a draw, no eliminations.")
                round_num += 1
                continue  # repeat round
            elif len(unique_moves) == 3:
                print("All three moves present. Round is a draw, no eliminations.")
                round_num += 1
                continue  # repeat round

            # Exactly two moves → determine winning move
            move1, move2 = unique_moves
            winning_move, losing_move = (move1, move2) if beats(move1, move2) else (move2, move1)

            # Eliminate losing players
            active_players = [p for p in active_players if current_moves[p] == winning_move]

            round_num += 1

        # Only one winner remains
        if len(active_players) == 1:
            winner = active_players[0]
            result = {p: ("win" if p == winner else "lose") for p in moves_dict}
        else:
            # Should rarely happen, but just in case
            result = {p: "draw" for p in moves_dict}

        return result


class Groups(BaseMode):
    """Team-based Rock Paper Scissors (to be implemented)."""
    def play_round(self, moves, groups, **kwargs):
        raise NotImplementedError("Groups mode not yet implemented.")
