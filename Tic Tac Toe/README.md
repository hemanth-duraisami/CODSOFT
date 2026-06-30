# Tic Tac Toe AI

This is a simple console-based Tic Tac Toe game built using Python as part of the **CODSOFT AI Internship**. The game allows a human player to play against an AI opponent that uses the **Minimax algorithm with Alpha-Beta Pruning**.

## About the Project

The goal of this project is to build an AI agent that can play Tic Tac Toe intelligently against a human player. The AI evaluates all possible moves and selects the best one, making it difficult to beat.

This project helps in understanding basic concepts of **game theory** and **search algorithms**.

## How the Game Works

* The player is **X**
* The AI is **O**
* The board has positions numbered from **1 to 9**
* Players take turns until someone wins or the game ends in a draw

## Features

* Human vs AI gameplay
* AI uses Minimax algorithm
* Alpha-Beta pruning for optimization
* Input validation for safe moves
* Detects win, loss, or draw automatically
* Simple terminal-based interface

## Game Rules

* Choose a position from 1 to 9 to place your move
* First player to get 3 in a row (horizontal, vertical, or diagonal) wins
* If all positions are filled without a winner, the game is a draw

## Technologies Used

* Python 3

## Project Structure

```text
TicTacToe/
├── tictactoe.py
└── README.md
```

## How to Run

1. Make sure Python 3 is installed on your system
2. Open terminal in the project folder
3. Run the program using:

```bash
python tictactoe.py
```

4. Start playing by entering numbers from 1 to 9

## Example

```text
1 2 3
4 5 6
7 8 9

Enter your move (1-9): 5

AI is thinking...
```

## Logic Overview

* The board is represented using a list of 9 elements
* Winning conditions are checked using predefined winning combinations
* The AI uses the Minimax algorithm to evaluate all possible moves
* Alpha-Beta pruning is used to improve performance by reducing unnecessary calculations

## Future Improvements

* Add difficulty levels (easy, medium, hard)
* Add a graphical interface using Tkinter or Pygame
* Allow player to choose X or O
* Add score tracking system

## Author

Developed as part of the **CODSOFT AI Internship**
