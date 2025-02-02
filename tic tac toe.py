import tkinter as tk
from tkinter import messagebox

def check_winner():
    for line in win_combinations:
        if buttons[line[0]]['text'] == buttons[line[1]]['text'] == buttons[line[2]]['text'] != '':
            winner_name = player1 if buttons[line[0]]['text'] == 'X' else player2
            messagebox.showinfo("Game Over", f"{winner_name} wins!")
            root.quit()
    if all(button['text'] != '' for button in buttons.values()):
        messagebox.showinfo("Game Over", "It's a draw!")
        root.quit()

def on_click(index):
    global turn
    if buttons[index]['text'] == '':
        buttons[index]['text'] = player_symbols[turn]
        check_winner()
        turn = 1 - turn

def start_game():
    global player1, player2, turn, buttons, win_combinations, player_symbols
    player1 = entry1.get()
    player2 = entry2.get()
    if not player1 or not player2:
        messagebox.showerror("Error", "Please enter both player names.")
        return
    
    player_symbols = ['X', 'O']
    turn = 0
    
    for widget in root.winfo_children():
        widget.destroy()
    
    root.geometry("600x600")
    
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            buttons[index] = tk.Button(root, text='', font=('Arial', 30), width=6, height=3, command=lambda idx=index: on_click(idx))
            buttons[index].grid(row=i, column=j)
    
    win_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")

player1_label = tk.Label(root, text="Player 1 Name: ")
player1_label.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

player2_label = tk.Label(root, text="Player 2 Name: ")
player2_label.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=2)

buttons = {}

root.mainloop()

