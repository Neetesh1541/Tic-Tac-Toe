import tkinter as tk
from tkinter import messagebox


class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Pro")
        self.root.geometry("700x820")
        self.root.resizable(False, False)
        self.root.configure(bg="#121826")

        self.win_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        self.player_names = ["Player 1", "Player 2"]
        self.player_symbols = ["X", "O"]
        self.scores = {"X": 0, "O": 0, "Draw": 0}

        self.mode_var = tk.StringVar(value="Two Players")
        self.turn = 0
        self.board = [""] * 9
        self.buttons = []
        self.game_active = False

        self.build_setup_screen()

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def build_setup_screen(self):
        self.clear_root()

        container = tk.Frame(self.root, bg="#121826")
        container.pack(expand=True, fill="both", padx=40, pady=40)

        tk.Label(
            container,
            text="Tic-Tac-Toe Pro",
            font=("Segoe UI", 34, "bold"),
            fg="#E6ECFF",
            bg="#121826",
        ).pack(pady=(30, 10))

        tk.Label(
            container,
            text="Play with a friend or challenge the AI.",
            font=("Segoe UI", 14),
            fg="#AAB6D6",
            bg="#121826",
        ).pack(pady=(0, 40))

        form = tk.Frame(container, bg="#1A2338", bd=0)
        form.pack(padx=40, pady=10, fill="x")

        tk.Label(
            form,
            text="Player 1 (X)",
            font=("Segoe UI", 12, "bold"),
            fg="#D6E0FF",
            bg="#1A2338",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(20, 6))
        self.entry1 = tk.Entry(
            form,
            font=("Segoe UI", 13),
            bg="#0F1628",
            fg="#F4F7FF",
            insertbackground="#F4F7FF",
            relief="flat",
        )
        self.entry1.insert(0, "Player 1")
        self.entry1.pack(fill="x", padx=20, pady=(0, 16), ipady=8)

        tk.Label(
            form,
            text="Mode",
            font=("Segoe UI", 12, "bold"),
            fg="#D6E0FF",
            bg="#1A2338",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(0, 6))

        mode_menu = tk.OptionMenu(form, self.mode_var, "Two Players", "Vs AI")
        mode_menu.config(
            font=("Segoe UI", 11),
            bg="#0F1628",
            fg="#F4F7FF",
            activebackground="#2C3D63",
            activeforeground="#FFFFFF",
            highlightthickness=0,
            bd=0,
        )
        mode_menu["menu"].config(
            font=("Segoe UI", 11),
            bg="#0F1628",
            fg="#F4F7FF",
            activebackground="#2C3D63",
            activeforeground="#FFFFFF",
        )
        mode_menu.pack(fill="x", padx=20, pady=(0, 16), ipady=4)

        tk.Label(
            form,
            text="Player 2 (O)",
            font=("Segoe UI", 12, "bold"),
            fg="#D6E0FF",
            bg="#1A2338",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(0, 6))
        self.entry2 = tk.Entry(
            form,
            font=("Segoe UI", 13),
            bg="#0F1628",
            fg="#F4F7FF",
            insertbackground="#F4F7FF",
            relief="flat",
        )
        self.entry2.insert(0, "Player 2")
        self.entry2.pack(fill="x", padx=20, pady=(0, 24), ipady=8)

        tk.Button(
            container,
            text="Start Game",
            font=("Segoe UI", 14, "bold"),
            bg="#4F7CFF",
            fg="#FFFFFF",
            activebackground="#6A90FF",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=18,
            pady=12,
            command=self.start_game,
        ).pack(pady=(24, 0))

    def start_game(self):
        player1 = self.entry1.get().strip() or "Player 1"
        mode = self.mode_var.get()

        if mode == "Vs AI":
            player2 = "AI"
        else:
            player2 = self.entry2.get().strip() or "Player 2"

        if player1 == player2:
            messagebox.showerror("Invalid Names", "Player names must be different.")
            return

        self.player_names = [player1, player2]
        self.game_mode = mode
        self.turn = 0
        self.board = [""] * 9
        self.game_active = True

        self.build_game_screen()
        self.refresh_board()

    def build_game_screen(self):
        self.clear_root()

        header = tk.Frame(self.root, bg="#121826")
        header.pack(fill="x", pady=(20, 8))

        tk.Label(
            header,
            text="Tic-Tac-Toe Pro",
            font=("Segoe UI", 24, "bold"),
            fg="#E6ECFF",
            bg="#121826",
        ).pack()

        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 14, "bold"),
            fg="#C9D7FF",
            bg="#121826",
        )
        self.status_label.pack(pady=(6, 16))

        self.score_label = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 12),
            fg="#9EB1E8",
            bg="#121826",
        )
        self.score_label.pack(pady=(0, 20))

        board_frame = tk.Frame(self.root, bg="#121826")
        board_frame.pack(pady=10)

        self.buttons = []
        for row in range(3):
            for col in range(3):
                idx = row * 3 + col
                button = tk.Button(
                    board_frame,
                    text="",
                    font=("Segoe UI", 34, "bold"),
                    width=4,
                    height=2,
                    bg="#1C2842",
                    fg="#E9EEFF",
                    activebackground="#2B3C63",
                    activeforeground="#FFFFFF",
                    relief="flat",
                    command=lambda i=idx: self.on_click(i),
                )
                button.grid(row=row, column=col, padx=8, pady=8)
                self.buttons.append(button)

        controls = tk.Frame(self.root, bg="#121826")
        controls.pack(pady=(24, 8))

        tk.Button(
            controls,
            text="New Round",
            font=("Segoe UI", 11, "bold"),
            bg="#4F7CFF",
            fg="#FFFFFF",
            activebackground="#6A90FF",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=12,
            pady=8,
            command=self.reset_round,
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            controls,
            text="Reset Scores",
            font=("Segoe UI", 11, "bold"),
            bg="#2D3B5F",
            fg="#FFFFFF",
            activebackground="#3E4E7A",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=12,
            pady=8,
            command=self.reset_scores,
        ).grid(row=0, column=1, padx=6)

        tk.Button(
            controls,
            text="Change Players",
            font=("Segoe UI", 11, "bold"),
            bg="#2D3B5F",
            fg="#FFFFFF",
            activebackground="#3E4E7A",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=12,
            pady=8,
            command=self.build_setup_screen,
        ).grid(row=0, column=2, padx=6)

    def refresh_board(self):
        for i, value in enumerate(self.board):
            self.buttons[i].config(text=value)

        current_name = self.player_names[self.turn]
        current_symbol = self.player_symbols[self.turn]
        self.status_label.config(text=f"{current_name}'s turn ({current_symbol})")
        self.score_label.config(
            text=(
                f"{self.player_names[0]} (X): {self.scores['X']}   |   "
                f"{self.player_names[1]} (O): {self.scores['O']}   |   "
                f"Draws: {self.scores['Draw']}"
            )
        )

    def on_click(self, index):
        if not self.game_active or self.board[index]:
            return

        self.board[index] = self.player_symbols[self.turn]
        result = self.check_winner(self.board)

        if result:
            self.end_round(result)
            return

        self.turn = 1 - self.turn
        self.refresh_board()

        if self.game_mode == "Vs AI" and self.turn == 1 and self.game_active:
            self.root.after(250, self.play_ai_turn)

    def play_ai_turn(self):
        if not self.game_active:
            return

        move = self.find_best_move()
        if move is None:
            return

        self.board[move] = "O"
        result = self.check_winner(self.board)

        if result:
            self.end_round(result)
            return

        self.turn = 0
        self.refresh_board()

    def check_winner(self, board):
        for a, b, c in self.win_combinations:
            if board[a] and board[a] == board[b] == board[c]:
                return board[a]
        if "" not in board:
            return "Draw"
        return None

    def end_round(self, result):
        self.game_active = False
        self.refresh_board()

        if result == "Draw":
            self.scores["Draw"] += 1
            self.status_label.config(text="It's a draw!")
            message = "It's a draw!"
        else:
            self.scores[result] += 1
            winner_name = self.player_names[0] if result == "X" else self.player_names[1]
            self.status_label.config(text=f"{winner_name} wins this round!")
            message = f"{winner_name} wins this round!"

        self.score_label.config(
            text=(
                f"{self.player_names[0]} (X): {self.scores['X']}   |   "
                f"{self.player_names[1]} (O): {self.scores['O']}   |   "
                f"Draws: {self.scores['Draw']}"
            )
        )

        if messagebox.askyesno("Round Over", f"{message}\n\nStart a new round?"):
            self.reset_round()

    def reset_round(self):
        self.board = [""] * 9
        self.turn = 0
        self.game_active = True
        self.refresh_board()

    def reset_scores(self):
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.reset_round()

    def minimax(self, board, is_maximizing):
        result = self.check_winner(board)
        if result == "O":
            return 1
        if result == "X":
            return -1
        if result == "Draw":
            return 0

        if is_maximizing:
            best_score = -10
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, False)
                    board[i] = ""
                    best_score = max(best_score, score)
            return best_score

        best_score = 10
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = self.minimax(board, True)
                board[i] = ""
                best_score = min(best_score, score)
        return best_score

    def find_best_move(self):
        best_score = -10
        best_move = None

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move


if __name__ == "__main__":
    root = tk.Tk()
    TicTacToeApp(root)
    root.mainloop()
