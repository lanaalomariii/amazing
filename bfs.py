from collections import deque


def find_shortest_path(
    grid: list,
    width: int,
    height: int,
    entry: tuple[int, int],
    exit_point: tuple[int, int]
) -> str:
    
    directions = {
        "N": (0, -1),
        "S": (0,  1),
        "E": (1,  0),
        "W": (-1, 0),
    }

    opposite = {
        "N": "S",
        "S": "N",
        "E": "W",
        "W": "E"
    }

    queue = deque()
    queue.append((entry, ""))

    visited = set()
    visited.add(entry)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == exit_point:
            return path

        for direction, (dx, dy) in directions.items():
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < width and 0 <= ny < height):
                continue

            if grid[ny][nx][opposite[direction]]:
                continue

            if (nx, ny) in visited:
                continue

            visited.add((nx, ny))
            queue.append(((nx, ny), path + direction))

    raise ValueError("No path found")
