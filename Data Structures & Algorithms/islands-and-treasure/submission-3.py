class Solution:
    def bfs(self, grid: List[List[int]], x: Tuple[int, int]) -> None:
        deltas = {-1, 1}
        queue = deque()
        queue.append(x)
        while queue:
            r,c = queue.popleft()
            d = grid[r][c]
            for delta in deltas:
                if 0 <= r+delta < len(grid) and d + 1 < grid[r+delta][c]:
                    grid[r+delta][c] = d + 1
                    queue.append((r+delta,c))

                if 0 <= c+delta < len(grid[0]) and d + 1 < grid[r][c+delta]:
                    grid[r][c+delta] = d + 1
                    queue.append((r,c+delta))
                

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 0:        # TREASURE - bfs out from here
                    self.bfs(grid, (i,j))
        