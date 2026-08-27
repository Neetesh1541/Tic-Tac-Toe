# Architecture

Tic-Tac-Toe Pro is a desktop application built with Python and Tkinter.

## Application flow

1. The setup screen collects player names and the selected game mode.
2. The game screen renders the 3x3 board and score information.
3. Player moves are validated before being written to the board.
4. `check_winner()` evaluates wins and draws after every move.
5. In Vs AI mode, the AI evaluates available moves with minimax.
6. Round and score state are updated before the next round starts.

## Main state

- `board`: nine board positions.
- `turn`: current player index.
- `scores`: wins for X, wins for O, and draws.
- `game_mode`: two-player or Vs AI mode.
- `game_active`: prevents moves after a round has ended.
