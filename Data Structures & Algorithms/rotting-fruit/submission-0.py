# https://neetcode.io/problems/rotting-fruit/question?list=neetcode150
from collections import deque
from typing import List, Tuple

class Solution:
    def bfs(self, days_to_rot: List[List[int]], x: Tuple[int, int]) -> None:
        deltas = {-1, 1}
        queue = deque()
        queue.append(x)
        while queue:
            r, c = queue.popleft()
            d = days_to_rot[r][c]
            for delta in deltas:
                if 0 <= r + delta < len(days_to_rot) and d + 1 < days_to_rot[r + delta][c]:
                    days_to_rot[r + delta][c] = d + 1
                    queue.append((r + delta, c))

                if 0 <= c + delta < len(days_to_rot[0]) and d + 1 < days_to_rot[r][c + delta]:
                    days_to_rot[r][c + delta] = d + 1
                    queue.append((r, c + delta))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        INF = 1001
        days_to_rot = []
        for i, row in enumerate(grid):
            days_to_rot.append([])
            for j, val in enumerate(row):
                if val == 0:
                    days_to_rot[i].append(-1) # empty cell can never rot
                elif val == 1:
                    days_to_rot[i].append(INF)  # 10 by 10 days_to_rot max distance = 100
                if val == 2:  # ROTTING FRUIT - bfs out from here
                    days_to_rot[i].append(0)
                    
        for i, row in enumerate(days_to_rot):
            for j, val in enumerate(row):
                if val == 0: 
                    self.bfs(days_to_rot, (i,j))

        max_time_to_rot = 0
        for i, row in enumerate(days_to_rot):
            max_time_to_rot = max(max_time_to_rot, max(row))

        if max_time_to_rot == INF:
            return -1
        else:
            return max_time_to_rot

grid = [[1,0,1],[0,2,0],[1,0,1]]
grid = [[1,1,0],[0,1,1],[0,1,2]]
print(Solution().orangesRotting(grid))