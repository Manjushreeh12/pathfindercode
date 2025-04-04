import pygame
from grid import Grid
from a_star import a_star
from bfs import bfs
from dfs import dfs
from dijkstra import dijkstra

# Pygame setup
pygame.init()
WIDTH, HEIGHT = 800, 600
UI_HEIGHT = 160  # Extra space for UI section
WINDOW_HEIGHT = HEIGHT + UI_HEIGHT  # Total window height

ROWS, COLS = 16, 16
NODE_SIZE = WIDTH // COLS

win = pygame.display.set_mode((WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Pathfinding Visualizer")

# Buttons
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 40
BUTTON_SPACING = 10
BUTTON_START_Y = HEIGHT + 40  # Below the grid

buttons = {
    "A*": pygame.Rect(20, BUTTON_START_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
    "BFS": pygame.Rect(190, BUTTON_START_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
    "DFS": pygame.Rect(360, BUTTON_START_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Dijkstra": pygame.Rect(530, BUTTON_START_Y, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Random Walls": pygame.Rect(20, BUTTON_START_Y + 60, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Clear": pygame.Rect(190, BUTTON_START_Y + 60, BUTTON_WIDTH, BUTTON_HEIGHT),
}

# Colors
WHITE, BLACK, BLUE, GREEN, RED, ORANGE, GRAY, DARK_GRAY = (
    (255, 255, 255),
    (0, 0, 0),
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (255, 165, 0),
    (200, 200, 200),
    (50, 50, 50),
)

def draw_buttons(win):
    """Draws the UI panel below the grid without flickering."""
    pygame.draw.rect(win, DARK_GRAY, (0, HEIGHT, WIDTH, UI_HEIGHT))  # UI Panel Background

    for text, rect in buttons.items():
        pygame.draw.rect(win, BLUE, rect, border_radius=5)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        win.blit(text_surface, text_rect)

def main():
    clock = pygame.time.Clock()
    grid = Grid(ROWS, COLS, NODE_SIZE, win)

    running = True

    while running:
        win.fill(WHITE)  # Clear screen
        grid.draw()  # Draw the grid
        draw_buttons(win)  # Draw buttons
        pygame.display.flip()  # ✅ Prevent flickering (double buffering)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if y < HEIGHT:  # Inside the grid
                    row, col = y // NODE_SIZE, x // NODE_SIZE
                    if event.button == 1:
                        grid.set_start(row, col)
                    elif event.button == 3:
                        grid.set_end(row, col)
                    elif event.button == 2:
                        grid.toggle_wall(row, col)

                # Click on a button
                for name, rect in buttons.items():
                    if rect.collidepoint(x, y):
                        if name == "A*" and grid.start and grid.end:
                            grid.reset_path()
                            a_star(grid, grid.start, grid.end)
                        elif name == "BFS" and grid.start and grid.end:
                            grid.reset_path()
                            bfs(grid, grid.start, grid.end)
                        elif name == "DFS" and grid.start and grid.end:
                            grid.reset_path()
                            dfs(grid, grid.start, grid.end)
                        elif name == "Dijkstra" and grid.start and grid.end:
                            grid.reset_path()
                            dijkstra(grid, grid.start, grid.end)
                        elif name == "Random Walls":
                            grid.generate_random_walls()
                        elif name == "Clear":
                            grid.clear_grid()

        clock.tick(60)  # Limit frame rate to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
