class Solution:
    def bfs(self, grid: List[List[str]], cell: Tuple[int,int]) -> int:
        queue = deque()
        queue.append(cell)
        while queue:
            i,j = queue.pop()
            if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1"):
                grid[i][j] = '0'
                queue.append((i+1,j))
                queue.append((i-1,j))
                queue.append((i,j-1))
                queue.append((i,j+1))
                

    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == "1":
                    self.bfs(grid, (i,j))
                    n_islands += 1
        return n_islands
                    