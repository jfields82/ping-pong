# ping-pong
# Pygame Ping Pong

A simple implementation of the classic Ping Pong game using Python and Pygame.

## Description

This project is a basic version of Ping Pong, created using Pygame. It features two paddles (one for the player and one for the AI opponent) and a ball. The game keeps track of the score and provides a simple yet entertaining gaming experience.

## Features

- Player-controlled paddle using keyboard input
- AI-controlled opponent
- Score tracking
- Ball physics with paddle and wall collisions
- Simple and clean visual design

## Requirements

- Python 3.x
- Pygame

## Installation

1. Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. Install Pygame using pip:

   ```
   pip install pygame
   ```

3. Clone this repository or download the source code.

## How to Play

1. Run the script:

   ```
   python ping_pong.py
   ```

2. Use the following controls:
   - 'W' key: Move your paddle (left side) up
   - 'S' key: Move your paddle (left side) down

3. Try to hit the ball with your paddle and score points when the opponent misses.

4. The game continues indefinitely. Close the window to exit the game.

## Customization

You can easily customize various aspects of the game by modifying the constants at the beginning of the script:

- `WIDTH` and `HEIGHT`: Change the size of the game window
- `PADDLE_WIDTH`, `PADDLE_HEIGHT`, and `PADDLE_SPEED`: Adjust paddle dimensions and speed
- `BALL_SIZE`, `BALL_SPEED_X`, and `BALL_SPEED_Y`: Modify ball size and speed

