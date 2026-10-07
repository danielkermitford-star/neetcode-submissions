# https://neetcode.io/problems/max-area-of-island/question
from collections import deque
from typing import List, Tuple

class Solution:
    def bfs(self, grid: List[List[int]], cell: Tuple[int, int]) -> int:
        deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        area = 1
        grid[cell[0]][cell[1]] = 0
        queue = deque([cell])
        while queue:
            r, c = queue.pop()
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    area += 1
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    max_area = max(max_area, self.bfs(grid, (i, j)))
        return max_area

grid=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]
print(Solution().maxAreaOfIsland(grid))