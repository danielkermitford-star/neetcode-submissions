import heapq
from math import inf
from typing import List, Dict


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        neighbor_of = [[] for _ in range(n)]
        for (u,v,w) in edges:
            neighbor_of[u].append((w,v))

        weight_to = {i:inf for i in range(n)}
        weight_to[src] = 0
        heap = []
        heapq.heappush(heap, (0,src))
        while heap:
            weight_to_u, u = heapq.heappop(heap)
            for weight_from_u_to_v, v in neighbor_of[u]:
                weight_to_u_then_v = weight_to_u + weight_from_u_to_v
                if weight_to_u_then_v < weight_to[v]:
                    weight_to[v] = weight_to_u_then_v
                    heapq.heappush(heap, (weight_to_u_then_v,v))

        for v,w in weight_to.items():
            if w == inf:
                weight_to[v] = -1
        return weight_to

n=5
edges=[[0,1,10],[0,2,3],[1,3,2],[2,1,4],[2,3,8],[2,4,2],[3,4,5]]
src=0
n=4
edges=[[0,1,5],[0,2,7],[1,2,2],[1,3,6],[2,3,4]]
src=1
print(Solution().shortestPath(n,edges,src))
