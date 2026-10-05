class Solution:
    
    def countServers(self, grid: List[List[int]]) -> int:
        # careful you don't overcount a server adjacent on both row and column

        # first compress grid into 2 lists
        # list of servers on each row and 
        # list of servers on each column
        servers_in_row = [[] for _ in range(len(grid))]
        servers_in_column = [[] for _ in range(len(grid[0]))]
               
        for i in range(len(grid)):
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
