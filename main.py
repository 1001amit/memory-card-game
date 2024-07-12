import tkinter as tk
import random
from tkinter import messagebox

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")
        
        self.buttons = []
        self.card_values = []
        self.first = None
        self.second = None
        self.matches = 0
        self.moves = 0
        
        self.setup_board(4, 4)  # Example: 4x4 grid

    def setup_board(self, rows, cols):
        self.reset_board()
        self.buttons = []
        self.card_values = []

        cards = list(range(1, (rows * cols) // 2 + 1)) * 2
        random.shuffle(cards)

        self.card_values = [cards[i:i + cols] for i in range(0, len(cards), cols)]

        for row in range(rows):
            button_row = []
            for col in range(cols):
                btn = tk.Button(self.root, width=10, height=5, command=lambda r=row, c=col: self.on_button_click(r, c))
                btn.grid(row=row, column=col)
                button_row.append(btn)
            self.buttons.append(button_row)

    def reset_board(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def on_button_click(self, row, col):
        if self.first and self.second:
            return
        btn = self.buttons[row][col]
        if not btn["text"]:
            btn["text"] = str(self.card_values[row][col])
            if not self.first:
                self.first = (row, col)
            else:
                self.second = (row, col)
                self.root.after(500, self.check_match)

    def check_match(self):
        row1, col1 = self.first
        row2, col2 = self.second
        if self.card_values[row1][col1] == self.card_values[row2][col2]:
            self.matches += 1
        else:
            self.buttons[row1][col1]["text"] = ""
            self.buttons[row2][col2]["text"] = ""
        self.first = None
        self.second = None
        self.moves += 1
        if self.matches == (len(self.card_values) * len(self.card_values[0])) // 2:
            self.end_game()

    def end_game(self):
        messagebox.showinfo("Congratulations!", f"You've matched all the cards in {self.moves} moves!")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()

