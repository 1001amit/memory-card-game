import tkinter as tk
import random
import time
from tkinter import messagebox

try:
    import winsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")
        self.root.configure(bg="black")
        
        self.buttons = []
        self.card_values = []
        self.card_colors = {
            1: "red",
            2: "blue",
            3: "green",
            4: "yellow",
            5: "orange",
            6: "purple",
            7: "pink",
            8: "cyan"
        }
        self.first = None
        self.second = None
        self.matches = 0
        self.moves = 0
        self.start_time = None

        self.top_frame = tk.Frame(self.root, bg="black")
        self.top_frame.pack(pady=10)

        self.timer_label = tk.Label(self.top_frame, text="Time: 0", font=("Helvetica", 14), bg="black", fg="white")
        self.timer_label.pack(side=tk.LEFT, padx=10)
        self.moves_label = tk.Label(self.top_frame, text="Moves: 0", font=("Helvetica", 14), bg="black", fg="white")
        self.moves_label.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.top_frame, text="Reset Game", font=("Helvetica", 14), command=self.setup_board)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.board_frame = tk.Frame(self.root, bg="black")
        self.board_frame.pack()

        self.setup_board(4, 4)

    def setup_board(self, rows=4, cols=4):
        self.reset_board()
        self.buttons = []
        self.card_values = []
        self.first = None
        self.second = None
        self.matches = 0
        self.moves = 0
        self.start_time = time.time()
        
        cards = list(range(1, (rows * cols) // 2 + 1)) * 2
        random.shuffle(cards)

        self.card_values = [cards[i:i + cols] for i in range(0, len(cards), cols)]

        for row in range(rows):
            button_row = []
            for col in range(cols):
                btn = tk.Button(self.board_frame, width=10, height=5, font=("Helvetica", 20), 
                                command=lambda r=row, c=col: self.on_button_click(r, c), bg="gray")
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
                self.board_frame.grid_rowconfigure(row, weight=1)
                self.board_frame.grid_columnconfigure(col, weight=1)
                button_row.append(btn)
            self.buttons.append(button_row)

        self.update_timer()

    def reset_board(self):
        for widget in self.board_frame.winfo_children():
            widget.destroy()

    def on_button_click(self, row, col):
        if self.first and self.second:
            return
        btn = self.buttons[row][col]
        if btn["bg"] == "gray":
            btn["bg"] = self.card_colors[self.card_values[row][col]]
            btn.config(state="disabled")
            self.play_sound("flip")
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
            self.play_sound("match")
        else:
            self.buttons[row1][col1]["bg"] = "gray"
            self.buttons[row2][col2]["bg"] = "gray"
            self.buttons[row1][col1].config(state="normal")
            self.buttons[row2][col2].config(state="normal")
            self.play_sound("nomatch")
        self.first = None
        self.second = None
        self.moves += 1
        self.moves_label.config(text=f"Moves: {self.moves}")
        if self.matches == (len(self.card_values) * len(self.card_values[0])) // 2:
            self.end_game()

    def end_game(self):
        elapsed_time = int(time.time() - self.start_time)
        messagebox.showinfo("Congratulations!", f"You've matched all the cards in {self.moves} moves and {elapsed_time} seconds!")
        self.play_sound("win")

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed_time}")
        self.root.after(1000, self.update_timer)

    def play_sound(self, sound_type):
        if SOUND_AVAILABLE:
            if sound_type == "flip":
                winsound.PlaySound("flip.wav", winsound.SND_ASYNC)
            elif sound_type == "match":
                winsound.PlaySound("match.wav", winsound.SND_ASYNC)
            elif sound_type == "nomatch":
                winsound.PlaySound("nomatch.wav", winsound.SND_ASYNC)
            elif sound_type == "win":
                winsound.PlaySound("win.wav", winsound.SND_ASYNC)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")
    game = MemoryGame(root)
    root.mainloop()
