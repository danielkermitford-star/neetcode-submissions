class Solution:
    def bfs(self, grid: List[List[int]], cell: Tuple[int, int], seen: set[Tuple[int, int]]) -> int:
        sum = 0
        queue = deque()
        queued = set()

        queue.append(cell)
        queued.add(cell)
        while queue:
            cr,cc = queue.pop()
            isolated = True
            for i in range(len(grid)):
                if i == cr:
                    continue
                elif grid[i][cc] == 1:
                    isolated = False
                    if (i,cc) not in seen: 
                        queue.append((i,cc))
                        queued.add((i,cc))
            for j in range(len(grid[0])):
                if j == cc:
                    continue
                elif grid[cr][j] == 1:
                    isolated = False
                    if (cr,j) not in seen: 
                        queue.append((cr,j))
                        queued.add((cr,j))
            if not isolated:
                sum += 1
        return sum

    def countServers(self, grid: List[List[int]]) -> int:
        # careful you don't overcount a server adjacent on both row and column

        # first compress grid into 2 lists
        # list of servers on each row and 
        # list of servers on each column
        servers_in_row = []
        servers_in_column = []
        for j in range(len(grid[0])):
            servers_in_column.append([])
        
        for i in range(len(grid)):
            servers_in_row.append([])
            for j in range(len(grid[0])):
                if grid[i][j]:
                    servers_in_row[i].append(j)
                    servers_in_column[j].append(i)

        connected = set()
        for i, columns in enumerate(servers_in_row):
            if len(columns) > 1:
                for j in columns:
                    connected.add((i,j)) 
        
        for j, rows in enumerate(servers_in_column):
            if len(rows) > 1:
                for i in rows:
                    # don't over count if already in same row with another server
                    if (i,j) not in connected:  
                        connected.add((i,j))

        return len(connected)
