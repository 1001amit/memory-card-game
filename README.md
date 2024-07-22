# Memory Card Game

A simple memory card matching game implemented in Python using the Tkinter library.

## Features

- Memory card game with a 4x4 grid.
- Color-coded cards for better visual distinction.
- Timer to track the duration of the game.
- Move counter to keep track of the number of moves made.
- Reset button to restart the game.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/1001amit/memory-card-game.git
    cd memory-card-game
    ```

2. Ensure you have Python installed. This game is compatible with Python 3.

3. Install Tkinter if it is not already installed:
    ```sh
    sudo apt-get install python3-tk
    ```

## Usage

1. Run the game:
    ```sh
    python main.py
    ```

2. The game window will open with a 4x4 grid of cards. Click on the cards to reveal their colors and find matching pairs.

3. The timer and move counter will keep track of your progress. The game ends when all pairs are matched.

4. Click the "Reset Game" button to restart the game at any time.

## Game Mechanics

- Click on a card to reveal its color.
- Click on a second card to try and find a match.
- If the cards match, they will remain revealed. If not, they will be hidden again.
- The game tracks the number of moves and the time taken to complete the game.
