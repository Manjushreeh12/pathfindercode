import pygame
import random

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)   # Start point
RED = (255, 0, 0)     # End point
BLUE = (0, 0, 255)    # Path
ORANGE = (255, 165, 0)  # Wall

class Grid:
    def __init__(self, rows, cols, node_size, win):
        self.rows = rows
        self.cols = cols
        self.node_size = node_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.end = None
        self.win = win  # Store the pygame window reference

    def draw(self):
        """Efficiently draws the grid and updates display only once."""
        for row in range(self.rows):
            for col in range(self.cols):
                color = WHITE  # Default: White
                if self.grid[row][col] == 1:
                    color = ORANGE  # Wall
                elif (row, col) == self.start:
                    color = GREEN  # Start point
                elif (row, col) == self.end:
                    color = RED  # End point
                elif self.grid[row][col] == 3:
                    color = BLUE  # Path

                pygame.draw.rect(
                    self.win,
                    color,
                    (col * self.node_size, row * self.node_size, self.node_size, self.node_size)
                )
                pygame.draw.rect(self.win, GRAY,  
                                 (col * self.node_size, row * self.node_size, self.node_size, self.node_size), 1)

    def set_start(self, row, col):
        """Sets the start point."""
        if self.grid[row][col] == 1:
            return
        self.start = (row, col)

    def set_end(self, row, col):
        """Sets the end point."""
        if self.grid[row][col] == 1:
            return
        self.end = (row, col)

    def toggle_wall(self, row, col):
        """Toggles a wall at the given cell."""
        if (row, col) == self.start or (row, col) == self.end:
            return
        self.grid[row][col] = 1 if self.grid[row][col] == 0 else 0

    def generate_random_walls(self):
        """Randomly generates walls with a 20% chance per cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) != self.start and (row, col) != self.end:
                    self.grid[row][col] = 1 if random.random() < 0.2 else 0

    def clear_grid(self):
        """Clears the grid, resetting all cells."""
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None

    def draw_path(self, path):
        """Marks the shortest path in the grid."""
        for row, col in path:
            if (row, col) != self.start and (row, col) != self.end:
                self.grid[row][col] = 3  # Mark path as BLUE

    def reset_path(self):
        """Removes any existing path visualization from the grid."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 3:
                    self.grid[row][col] = 0

    def get_neighbors(self, row, col):
        """Returns the valid neighbors of a given node."""
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] != 1:
                neighbors.append((r, c))

        return neighbors
