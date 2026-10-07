class Solution:            

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        deltas = [(di,dj) for di in (-1,0,1) for dj in (-1,0,1) if not (di == 0 and dj == 0)] # all 8 directions
        # deltas = [(-1,0), (+1,0), (0,-1), (0,+1)] # four direction

        max_r = len(grid) - 1
        max_c = len(grid[0]) - 1
        visited = set()
        queue = deque([(0,0,1)]) # d = 1 to count the start (0,0)
        while queue:
            r, c, d = queue.popleft()
            if 0 <= r <= max_r and 0 <= c <= max_c \
                and (r, c) not in visited and grid[r][c] == 0:
                if r == max_r and c == max_c:
                    return d
                visited.add((r,c))
                for dr, dc in deltas:
                    queue.append((r + dr, c + dc, d + 1))
        return -1
                

        