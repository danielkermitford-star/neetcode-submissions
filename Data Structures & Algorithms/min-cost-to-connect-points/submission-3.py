import heapq
from typing import List

# Kruskal's Union Find Algorithm

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Manhattan distance
        def dM(i: float, j: float) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        heap = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, [dM(i, j), i, j])

        # find
        def root(i: int) -> int:
            if parent[i] != i:
                parent[i] = root(parent[i])
            return parent[i]

        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]

        cost = 0
        unions = 0
        while unions < n-1:     # n-1 unions and they're all combined
            dist, u, v = heapq.heappop(heap)
            u, v = root(u), root(v)
            if u != v:
                unions += 1
                cost += dist
                # attach the smaller to the larger one
                if size[u] < size[v]:
                    parent[u] = v
                    size[v] += size[u]
                else :
                    parent[v] = u
                    size[u] += size[v]

        return cost


points=[[0,0],[2,2],[3,3],[2,4],[4,2]]
points=[[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))