import heapq
import pygame

def dijkstra(grid, start, end):
    rows, cols = grid.rows, grid.cols  # Get grid dimensions
    start_pos = start  # ✅ Correct: (row, col) tuple
    end_pos = end  # ✅ Correct: (row, col) tuple

    # Priority queue
    pq = [(0, start_pos)]  # (cost, (row, col))
    distances = {start_pos: 0}
    came_from = {}

    visited = set()  # Track visited nodes

    while pq:
        current_cost, (r, c) = heapq.heappop(pq)

        if (r, c) in visited:
            continue  # Skip already visited nodes

        visited.add((r, c))

        if (r, c) == end_pos:
            break  # Stop when we reach the end node

        for neighbor in grid.get_neighbors(r, c):
            nr, nc = neighbor
            new_cost = current_cost + 1  # Uniform cost

            if (nr, nc) not in distances or new_cost < distances[(nr, nc)]:
                distances[(nr, nc)] = new_cost
                heapq.heappush(pq, (new_cost, (nr, nc)))
                came_from[(nr, nc)] = (r, c)

                # ✅ Visualizing the search process
                if (nr, nc) != start_pos and (nr, nc) != end_pos:
                    grid.grid[nr][nc] = 2  # Mark as visited
                    grid.draw()
                    pygame.time.delay(10)  # Animation delay

    # ✅ Reconstruct and visualize the shortest path
    path = []
    current = end_pos
    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.reverse()  # Correct order

    grid.draw_path(path)  # ✅ Visualize the shortest path
