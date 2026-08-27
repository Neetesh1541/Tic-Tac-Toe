# AI Strategy

The Vs AI mode uses the minimax algorithm.

## How it works

The AI treats `O` as the maximizing player and `X` as the minimizing player. It recursively explores available moves until it reaches a win, loss, or draw state.

Scores are assigned as follows:

- AI win: `+1`
- Human win: `-1`
- Draw: `0`

The move with the highest score is selected. Because Tic-Tac-Toe has a small state space, exhaustive minimax is fast enough for this desktop game and produces an unbeatable opponent when implemented correctly.
