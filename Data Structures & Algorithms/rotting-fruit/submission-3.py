# https://neetcode.io/problems/rotting-fruit/question?list=neetcode150
from collections import deque
from typing import List, Tuple, Set


class Solution:
    def bfs(self, grid: List[List[int]], rotten: Set[Tuple[int, int]]) -> int:
        neighbor_deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        days_to_rot = 0
        just_rotted = set(rotten)  # set of positions in grid of just rotted oranges
                                    # alternatively just_rotten = rotten.copy()
        while just_rotted:          # continue until there are no new oranges rot
            unrotted_neighbors = set() # don't need to change grid to avoid duplicates if this is a set
            for r, c in just_rotted:    # position or just_rotted orange
                for dr, dc in neighbor_deltas:
                    nr, nc = r + dr, c + dc     # neighbor or just rotted orange
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2        # its now rotten - don't count it again
                        unrotted_neighbors.add((nr, nc))    # above line optional with set of unrotted_neighbors
            just_rotted = unrotted_neighbors
            # (! is set union; & is set intersection)
            rotten.update(just_rotted)  # alternatively rotten |= just_rotten
            if just_rotted:
                days_to_rot += 1  # if all oranges were already rotted days_to_rot == 0
        return days_to_rot


    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        n_oranges = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:    # rotten fruit
                    rotten.add((i, j))
                    n_oranges += 1
                elif val == 1:
                    n_oranges += 1

        days_to_rot = self.bfs(grid, rotten)
        if len(rotten) < n_oranges:
            return -1
        else:
            return days_to_rot


grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
print(Solution().orangesRotting(grid))