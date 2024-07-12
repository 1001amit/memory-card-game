import tkinter as tk
import random
import time
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
        self.start_time = None
        
        # Create a frame for the labels
        self.top_frame = tk.Frame(self.root)
        self.top_frame.grid(row=0, column=0, columnspan=4, pady=10)

        # Timer and Moves Labels
        self.timer_label = tk.Label(self.top_frame, text="Time: 0", font=("Helvetica", 14))
        self.timer_label.grid(row=0, column=0, padx=10)
        self.moves_label = tk.Label(self.top_frame, text="Moves: 0", font=("Helvetica", 14))
        self.moves_label.grid(row=0, column=1, padx=10)

        self.setup_board(4, 4)  # Example: 4x4 grid

    def setup_board(self, rows, cols):
        self.reset_board()
        self.buttons = []
        self.card_values = []
        self.first = None
        self.second = None
        self.matches = 0
        self.moves = 0
        self.start_time = time.time()  # Start the timer
        
        cards = list(range(1, (rows * cols) // 2 + 1)) * 2
        random.shuffle(cards)

        self.card_values = [cards[i:i + cols] for i in range(0, len(cards), cols)]

        for row in range(rows):
            button_row = []
            for col in range(cols):
                btn = tk.Button(self.root, width=10, height=5, font=("Helvetica", 20), 
                                command=lambda r=row, c=col: self.on_button_click(r, c))
                btn.grid(row=row+1, column=col, padx=5, pady=5)  # Adjust row index to avoid overlap with top_frame
                button_row.append(btn)
            self.buttons.append(button_row)

        self.update_timer()

    def reset_board(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()
        # No need to repack timer and moves labels, as they are in top_frame
        self.top_frame.grid(row=0, column=0, columnspan=4, pady=10)

    def on_button_click(self, row, col):
        if self.first and self.second:
            return
        btn = self.buttons[row][col]
        if not btn["text"]:
            btn["text"] = str(self.card_values[row][col])
            btn.config(state="disabled")
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
            self.buttons[row1][col1].config(state="normal")
            self.buttons[row2][col2].config(state="normal")
        self.first = None
        self.second = None
        self.moves += 1
        self.moves_label.config(text=f"Moves: {self.moves}")
        if self.matches == (len(self.card_values) * len(self.card_values[0])) // 2:
            self.end_game()

    def end_game(self):
        elapsed_time = int(time.time() - self.start_time)
        messagebox.showinfo("Congratulations!", f"You've matched all the cards in {self.moves} moves and {elapsed_time} seconds!")

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed_time}")
        self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
