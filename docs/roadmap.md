RPS-LAN Flow (MVP)
1. Lobby Menu
Show available modes:
1v1
Free-for-All (ask number of players N ≥ 2)
Groups (later)

2. Game Setup
Based on selection:
1v1: expect exactly 2 players.
FFA: wait for N players to join (N chosen before start).
Groups: configure groups (later).

3. Gameplay Round
Broadcast “ready → make your move”.
Each player submits: "rock" / "paper" / "scissors".
Wait until all moves are received.

4. Winner Decision
Call the appropriate mode-specific function.
Resolve result (win, lose, draw).
Send result to all players.

5. Game End
For now → one round only (simplest MVP).
Later → add “Play Again?” or best-of-N rounds.




game_logic.py → atomic rules only (rock beats scissors, etc.).
modes.py → uses game_logic to implement higher-level rules (1v1, FFA, Groups).
game_manager.py → server orchestration, decides when to call which mode.
Tests are split so you can test:
Pure rules → test_game_logic.py.
Mode rules → test_modes.py.





# Game Modes for RPS-LAN<br>
1. 1v1<br>
Classic Rock-Paper-Scissors.<br>
Exactly 2 players.<br>
Winner decided by direct comparison.<br>

2. Free-for-All (FFA)<br>
Any number of players N ≥ 2.<br>
All players throw moves simultaneously.<br>
Rules (like we discussed):<br>
All same → draw.<br>
All 3 moves present → draw.<br>
Exactly 2 moves present → one move dominates, all players with that move win.<br>

3. Groups (Team RPS)<br>
Players divided into teams before match starts.<br>
Each team’s move decided either by:<br>
Majority vote (team move = most common among members).<br>
Coordinator selection (a captain picks).<br>
Teams face off using standard rules.<br>

# Core Logic
> offline, no network yet
## common/game_logic.py:
Function decide_winner(move1, move2) > returns winner or draw.<br>
Unit testing in tests/test_game_logic.py.<br>
Play RPS locally by calling functions.


Modes:
2v2
free-for-

































Phase 2: Basic Networking (text only)

Setup server/server_main.py: accepts 2 clients via TCP sockets.

Setup client/client_main.py: connects to server, sends/receives text moves.



































Define message protocol in common/protocol.py (JSON is simplest).
✅ Two terminals can play RPS over LAN.

Phase 3: Modular Game Manager

Add server/game_manager.py:

Handles multiple rounds, keeps track of scores.

Add server/handler.py:

Manages client connections in threads.
✅ Server is more structured, not just spaghetti sockets.

Phase 4: GUI (PC/Laptop)

Implement client/gui.py with Kivy:

Buttons for Rock, Paper, Scissors.

Display result + running score.

client/client_main.py becomes GUI entrypoint.
✅ Now it feels like a real game, not just terminals.

Phase 5: Android Support

Setup android/buildozer.spec.

Package the Kivy client as APK → test on phones.

Ensure LAN discovery works on WiFi (same network).
✅ Seniors can pull out phones and play during breaks.

Phase 6: Polish & Extras (optional, if time allows)

Scoreboard: persistent scores, leaderboard.

Lobby system: more than 2 players, quick matchmaking.

Custom skins/themes: add fun GUI polish (e.g., emojis for moves ✊ ✋ ✌️).

Spectator mode: extra clients can watch matches.