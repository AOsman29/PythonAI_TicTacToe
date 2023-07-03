import tkinter as tk
from tkinter import messagebox

# set up game board
board = [' ' for _ in range(9)] 

def score(board):
    if is_victory('X'):
        return -1
    if is_victory('O'):
        return 1
    return 0

def minimax(board, depth, maximizingPlayer):
    if is_victory('O') or is_victory('X') or is_draw():
        return score(board)

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False)
                board[i] = ' '
                maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = float('inf')
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True)
                board[i] = ' '
                minEval = min(minEval, eval)
        return minEval
    
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False
    
def get_free_spaces():
    return [i for i, x in enumerate(board) if x == " "]

def ai_move():
    maxEval = float('-inf')
    move = 0
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = 'O'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > maxEval:
                maxEval = eval
                move = i
    board[move] = 'O'

def click(row, col):
    index = 3 * row + col
    if board[index] == ' ':
        board[index] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        if not is_victory('X') and not is_draw():
            ai_move()
            update_buttons()
        check_game_state()


def update_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[3*i + j])
            if board[3*i + j] != ' ':
                buttons[i][j].config(state=tk.DISABLED)

def check_game_state():
    if is_victory('X'):
        messagebox.showinfo("Game over", "Player 1 Wins!")
        root.quit()
    elif is_victory('O'):
        messagebox.showinfo("Game over", "Player 2 Wins!")
        root.quit()
    elif is_draw():
        messagebox.showinfo("Game over", "It's a draw!")
        root.quit()

root = tk.Tk()

buttons = [[tk.Button(root, text=' ', font=('default', 20), height=3, width=6,
                      command=lambda row=row, col=col: click(row, col)) 
            for col in range(3)] for row in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
