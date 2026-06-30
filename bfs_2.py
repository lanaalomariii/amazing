from collections import deque


def find_shortest_path(maze: list, width: int, height: int,
                       entry: tuple[int, int], exit_p: tuple[int, int]
                       ) -> str:
    directions = {"N": (0, -1), "S": (0,  1), "E": (1,  0), "W": (-1, 0)}
    queue = deque()
    queue.append(entry)
    visited = set()
    visited.add(entry)
    while queue:
        current = queue.popleft()
        if current == exit_p:
            return path

