import pygame
import numpy as np
import time

# Set up the grid
width, height = 800, 600
rows, cols = 80, 60
cell_size = width // rows

# Initialize the grid with random values
grid = np.random.choice([0, 1], size=(rows, cols))

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Function to update the grid based on the rules of the game
def update_grid(grid):
    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):
            neighbors = (
                grid[i - 1:i + 2, j - 1:j + 2].sum() - grid[i, j]
            )  # Sum of neighbors excluding the center cell

            # Apply Conway's rules
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    return new_grid

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Update and draw the grid
    grid = update_grid(grid)
    for i in range(rows):
        for j in range(cols):
            color = white if grid[i, j] == 1 else black
            pygame.draw.rect(
                screen, color, (j * cell_size, i * cell_size, cell_size, cell_size)
            )

    pygame.display.flip()
    time.sleep(0.1)  # Adjust the speed of the game by changing the sleep duration

pygame.quit()