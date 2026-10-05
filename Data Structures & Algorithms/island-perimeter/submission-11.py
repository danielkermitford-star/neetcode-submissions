class Solution:

    # Every permiter line is adjacent to exactly 
    # one square of the island!

    # BFS - continue until the queue is empty
    # for all four neighbors: if it's a 0 add 1 to perimiter
    # Otherwise, it's a 1, add the square to the queue

    def bfs(self, grid: List[List[int]], square: Tuple[int, int]) -> int:
        perimiter = 0
        seen = set()
        queue = deque()
        queue.append(square)
        while queue:
            i, j = queue.pop()
            if (i,j) in seen:
                continue
            else:
                seen.add((i,j))
            
            if i <= 0 or   grid[i-1][j] == 0:     perimiter += 1
            else: queue.append((i-1, j))

            if j <= 0 or   grid[i][j-1] == 0:     perimiter += 1
            else: queue.append((i, j-1))
            
            if i >= len(grid)-1 or grid[i+1][j] == 0: perimiter += 1
            else:         queue.append((i+1, j))

            if j >= len(grid[0])-1 or grid[i][j+1] == 0: perimiter += 1
            else:         queue.append((i, j+1))

        return perimiter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # find part of the island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return self.bfs(grid, (i, j))
                    
        