import heapq

def a_star(grid, start, end):
    rows, cols = grid.rows, grid.cols

    # Ensure start and end are tuples (row, col)
    start_pos = start  # Already a tuple
    end_pos = end  # Already a tuple

    open_set = [(0, start_pos)]  # (f_score, (row, col))
    came_from = {}
    g_score = {start_pos: 0}
    f_score = {start_pos: heuristic(start_pos, end_pos)}

    while open_set:
        _, (r, c) = heapq.heappop(open_set)

        if (r, c) == end_pos:
            break

        for neighbor in grid.get_neighbors(r, c):
            nr, nc = neighbor
            tentative_g_score = g_score[(r, c)] + 1

            if (nr, nc) not in g_score or tentative_g_score < g_score[(nr, nc)]:
                g_score[(nr, nc)] = tentative_g_score
                f_score[(nr, nc)] = tentative_g_score + heuristic((nr, nc), end_pos)
                heapq.heappush(open_set, (f_score[(nr, nc)], (nr, nc)))
                came_from[(nr, nc)] = (r, c)

    # Reconstruct path
    path = []
    current = end_pos
    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.reverse()
    grid.draw_path(path)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance
