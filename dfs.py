import pygame

def dfs(grid, start, end):
    rows, cols = grid.rows, grid.cols
    start_pos = start  # ✅ Correct: (row, col) tuple
    end_pos = end  # ✅ Correct: (row, col) tuple

    stack = [start_pos]
    came_from = {start_pos: None}
    visited = set()  # Track visited nodes

    while stack:
        r, c = stack.pop()

        if (r, c) in visited:
            continue  # Skip already visited nodes

        visited.add((r, c))

        # ✅ If we reached the end, stop searching
        if (r, c) == end_pos:
            break

        for neighbor in grid.get_neighbors(r, c):
            if neighbor not in came_from:
                stack.append(neighbor)
                came_from[neighbor] = (r, c)

                # ✅ Visualizing the search process
                if neighbor != start_pos and neighbor != end_pos:
                    grid.grid[neighbor[0]][neighbor[1]] = 2  # Mark as visited
                    grid.draw()
                    pygame.time.delay(10)  # Animation delay

    # ✅ Reconstruct and visualize the shortest path
    path = []
    current = end_pos
    while current in came_from and came_from[current] is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()  # Correct order
    grid.draw_path(path)  # ✅ Visualize the shortest path
