import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")
        
        self.buttons = []
        self.card_values = []
        
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
        btn = self.buttons[row][col]
        btn["text"] = str(self.card_values[row][col])

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
