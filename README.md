# Simple Shooter Game

## Description
A simple 2D shooter game implemented using Python and Pygame. The player controls a blue square and must shoot a red enemy while avoiding enemy bullets. The game features a main menu, player and enemy movement, shooting mechanics, and a life bar for both the player and the enemy.

## Features
- **Main Menu:** A start button that transitions to the game loop.
- **Player Movement:** Move the player character left and right using the arrow keys.
- **Shooting Mechanics:** Shoot bullets by pressing the Enter key.
- **Enemy Movement:** The enemy moves randomly and shoots bullets at the player.
- **Life Bars:** Displays the life of both the player and the enemy.
- **Game Over:** Displays a game over message when either the player or the enemy's life reaches zero.

## Setup
1. Ensure Python and Pygame are installed. You can install Pygame via pip:
   ```bash
   pip install pygame
   ```

2. Save the provided Python script as Shgame.py

3. Run the game using:
   ```bash
   python Shgame.py
   ```

## Controls
- Left Arrow: Move player left.
- Right Arrow: Move player right.
- Enter: Shoot bullets.

## Code Overview
### Initialization
- pygame.init() - Initializes Pygame modules.
- screen - Sets up the display screen.
- clock - Manages the game frame rate.

### Functions
- draw_player() - Draws the player and its life bar.
- draw_enemy() - Draws the enemy and its life bar.
- draw_bullets() - Draws all bullets on the screen.
- update_bullets() - Updates bullet positions and removes bullets off-screen.
- check_collision() - Checks for collisions between bullets and player/enemy.
- draw_life() - Draws the life bar with a label.
- enemy_shoot() - Handles the enemy's shooting behavior.
- move_enemy() - Moves the enemy randomly.
- game_over() - Displays the game over message and exits.
- draw_button() - Draws a styled button.
- main_menu() - Displays the main menu with a start button.
- game_loop() - Main game loop managing game logic and rendering.
