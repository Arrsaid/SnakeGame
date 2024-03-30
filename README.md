# Python Turtle Snake Game

This Snake Game is a simple, classic game developed in Python using the Turtle graphics library. The game implements the principles of Object-Oriented Programming (OOP), making it an excellent project for learning and teaching purposes. The project is structured into several modules - `food.py`, `snake.py`, `scoreboard.py`, and utilizes a `data.txt` file for persisting the highest score achieved across sessions.

## Features

- Classic Snake gameplay experience.
- Customizable snake and food objects.
- Real-time score tracking with high score persistence.
- Clean and modular code using Object-Oriented Programming (OOP) principles.

## Modules

### `snake.py`
The core logic for the snake's behavior, including movement, growth, and collision detection.

### `food.py`
Defines the food object that the snake will consume. Random placement logic included.

### `scoreboard.py`
Manages the score display and high score tracking, reading from and writing to `data.txt`.

### `data.txt`
A simple text file to store the highest score obtained between game sessions.

## Installation

To run this game, ensure you have Python installed on your system. No external libraries are required beyond the standard Turtle graphics library included with Python.

```bash
git clone <Your-Project-Repository-URL>
cd <Your-Project-Directory>
python main.py
