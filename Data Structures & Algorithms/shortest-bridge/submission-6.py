#https://neetcode.io/problems/shortest-bridge/question
from collections import deque
from typing import List, Tuple, Set


class Solution:
    # 1) use bfs to find an island of 1's
    # 2) use a second bfs to find the shortest path from any point
    #       on the island to any other 1 - not on the fist island
    #       - through the 0's of the water.
    #       Start with all the 1's from the island into the new queue

    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # change all the 1's on the island to 2's
    def bfs_flood_fill_island(self, grid: List[List[int]], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
        seen = set()
        queue = deque([start])
        while queue:
            r, c = queue.popleft()
            if grid[r][c] == 1:
                grid[r][c] = 2
                seen.add((r, c))
                for dx, dy in self.deltas:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                # if i > 0 and grid[i - 1][j] == 1: queue.append((i - 1, j))
                # if j > 0 and grid[i][j - 1] == 1: queue.append((i, j - 1))
                # if i < len(grid) - 1 and grid[i + 1][j] == 1: queue.append((i + 1, j))
                # if j < len(grid[0]) - 1 and grid[i][j + 1] == 1: queue.append((i, j + 1))
        return seen

    def bfs_shortest_path_to_island(self, grid: List[List[int]], seen: Set[Tuple[int, int]]) -> int:
        queue = deque([c + (0,) for c in seen])
        seen.clear()
        while queue:
            r, c, d = queue.popleft()
            if (r, c) in seen:
                continue
            elif grid[r][c] == 1:
                return d
            seen.add((r, c))
            for dx, dy in self.deltas:
                nr, nc = r + dx, c + dy
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    queue.append((nr, nc, d+1))
            # if i > 0:                   queue.append((i - 1, j, d + 1))
            # if j > 0:                   queue.append((i, j - 1, d + 1))
            # if i < len(grid) - 1:        queue.append((i + 1, j, d + 1))
            # if j < len(grid[0]) - 1:     queue.append((i, j + 1, d + 1))
        return -1  # never found the other island

    def shortestBridge(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    island = self.bfs_flood_fill_island(grid, (i, j))
                    return self.bfs_shortest_path_to_island(grid, island)   - 1
                    # returns the number of 1's we need to add which is one less than the distance to the next island

grid=[[1,0],[0,1]]
print(Solution().shortestBridge(grid))