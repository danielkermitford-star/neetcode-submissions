class Solution:
    def bfs(self, grid: List[List[int]], cell: Tuple[int,int]) -> int:
        area = 0
        queue = deque()
        queue.append(cell)
        while queue:
            i,j = queue.pop()
            if (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1):
                area += 1
                grid[i][j] = '0'
                queue.append((i+1,j))
                queue.append((i-1,j))
                queue.append((i,j-1))
                queue.append((i,j+1))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    max_area = max(max_area, self.bfs(grid, (i,j)))
        return max_area
                    
        