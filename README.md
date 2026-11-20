# Snake Game

Classic Snake game built with **Python** and **Pygame**, featuring progressive difficulty levels.

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python" width="40" height="40" />
</p>

## Features

* **Progressive Level System:** Starts at a base speed of `6 FPS` and levels up every **2 apples eaten** (20 points), increasing the snake's movement speed.
* **Real-Time HUD:** Displays current score and active level on screen.
* **Grid-Based Movement:** Smooth step-by-step movement with 180-degree turn prevention to avoid accidental self-collisions.

## Project Structure

```text
snake-game-py/
├── main.py
└── README.md
```

## Requirements & Setup

1. Make sure **Python 3.8+** is installed on your machine.
2. Clone the repository:
   ```bash
   git clone [https://github.com/nicolleqa/snake-game-py.git](https://github.com/nicolleqa/snake-game.git)
   cd snake-game-py
   ```
3. Install `pygame`:
   ```bash
   pip install pygame
   ```


## How to Play

Run the main script from your terminal:

```bash
python main.py
```
*(Or `py main.py` on Windows)*

### Controls

| Key | Action |
| :--- | :--- |
| **Arrow Keys** (`Up`, `Down`, `Left`, `Right`) | Move the snake |
| **`SPACE`** | Restart the game (on the *Game Over* screen) |
| **`ESC`** | Quit the game (on the *Game Over* screen) |