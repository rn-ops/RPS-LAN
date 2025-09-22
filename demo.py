from common.modes import OneVsOne, FreeForAll

def run_demo():
    print("=== RPS-LAN Demo ===")
    print("Select mode: ")
    print("1. 1v1")
    print("2. Free-for-All")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        mode = OneVsOne()
        moves = {
            "p1": input("Player 1 move (rock/paper/scissors): ").strip().lower(),
            "p2": input("Player 2 move (rock/paper/scissors): ").strip().lower()
        }
        result = mode.play_round(moves)
        print("\n--- Results ---")
        for player, outcome in result.items():
            print(f"{player}: {outcome}")

    elif choice == "2":
        mode = FreeForAll()
        num_players = int(input("Number of players (>=2): "))
        if num_players < 2:
            print("FFA requires at least 2 players.")
            return

        # Initialize active players
        active_players = [f"p{i}" for i in range(1, num_players + 1)]
        player_moves = {}

        # First round: get initial moves
        for p in active_players:
            move = input(f"{p} move (rock/paper/scissors): ").strip().lower()
            player_moves[p] = move

        round_num = 1
        while len(active_players) > 1:
            print(f"\n--- Round {round_num} ---")
            # Collect moves for current active players
            for p in active_players:
                move = input(f"{p} move (rock/paper/scissors): ").strip().lower()
                player_moves[p] = move

            # Play round
            current_moves = {p: player_moves[p] for p in active_players}
            result = mode.play_round(current_moves)

            # Show round results
            for p in active_players:
                print(f"{p}: {result[p]}")

            # Update active players
            active_players = [p for p in active_players if result[p] == "win"]
            if len(active_players) == 0:
                print("All players eliminated. Round draw!")
                break
            elif len(active_players) == 1:
                print(f"\nWinner: {active_players[0]}!")
                break

            round_num += 1

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    run_demo()
