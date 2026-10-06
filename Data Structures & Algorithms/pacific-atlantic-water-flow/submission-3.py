from collections import deque
from typing import List, Deque, Tuple, Set


class Solution:
    def bfs(self, heights: List[List[int]], pathtoOcean: Set[Tuple[int,int]]):
        queue = deque(pathtoOcean)
        pathtoOcean.clear()

        while queue:
            i, j = queue.popleft()
            if (i,j) in pathtoOcean:
                continue
            else:
                pathtoOcean.add((i,j))
            if i > 0 and                    heights[i][j] <= heights[i - 1][j]: queue.append((i - 1, j))
            if j > 0 and                    heights[i][j] <= heights[i][j - 1]: queue.append((i, j - 1))
            if i + 1 < len(heights) and     heights[i][j] <= heights[i + 1][j]: queue.append((i + 1, j))
            if j + 1 < len(heights[0]) and  heights[i][j] <= heights[i][j + 1]: queue.append((i, j + 1))

        return pathtoOcean

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pathtoPacific = set([(i,j) for i, row in enumerate(heights) for j,_ in enumerate(row) if i == 0 or j == 0])
        pathtoAtlantic = set([(i,j) for i, row in enumerate(heights) for j,_ in enumerate(row) if i+1 == len(heights) or j+1 == len(heights[0])])
        self.bfs(heights, pathtoPacific)
        self.bfs(heights, pathtoAtlantic)

        return [list(i) for i in pathtoPacific & pathtoAtlantic]

heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
# heights=[[1],[1]]
print(Solution().pacificAtlantic(heights))
