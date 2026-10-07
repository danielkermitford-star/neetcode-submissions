# https://neetcode.io/problems/islands-and-treasure/question?list=neetcode150
from collections import deque
from typing import List, Tuple


class Solution:
    def bfs(self, grid: List[List[int]], x: Tuple[int, int]) -> None:
        deltas = [(-1,0), (1,0), (0,-1), (0,1)]
        max_row = len(grid) -1
        max_col = len(grid[0]) -1
        queue = deque([x])
        while queue:
            r, c = queue.popleft()
            d = grid[r][c]
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= max_row and 0 <= nc <= max_col and d + 1 < grid[nr][nc]:
                    grid[nr][nc] = d + 1
                    queue.append((nr, nc))

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:  # TREASURE - bfs out from here
                    self.bfs(grid, (i, j))

grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Solution().islandsAndTreasure(grid)
print(*grid, sep='\n')