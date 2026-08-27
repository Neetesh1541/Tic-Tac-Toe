# Development Notes

## Runtime

The project uses Python 3 and Tkinter. Tkinter is part of the standard Python distribution on most desktop installations.

## Code structure

The current implementation keeps the UI, game state, rules, and AI logic inside the `TicTacToeApp` class so the project remains easy to run as a small desktop application.

## Before publishing changes

- Run the application from a clean Python environment.
- Test both Two Players and Vs AI modes.
- Verify win, loss, and draw scenarios.
- Verify New Round and Reset Scores behavior.
- Avoid committing generated `__pycache__` files.
