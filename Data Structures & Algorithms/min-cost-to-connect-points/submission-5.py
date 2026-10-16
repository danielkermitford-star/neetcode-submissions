import heapq
import math
from typing import List

# based on https://cp-algorithms.com/geometry/manhattan-distance.html

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        I_SQRT_2 = 1/math.sqrt(2)

        # Manhattan Distance
        def mD(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        # find set of edges
        edges = set()

        points_with_index = [[] for _ in range(n)]
        for i,(x,y) in enumerate(points):
            points_with_index[i] = (x,y,i)

        for _ in range(8):
            points_rotated_clockwise_45_degrees = [(0,0,i) for i in points]

            for x,y,i in points_with_index:
                points_rotated_clockwise_45_degrees[i] = ((y + x)*I_SQRT_2, (y - x)*I_SQRT_2, i)

            sorted_rotated_points = sorted(points_rotated_clockwise_45_degrees)
            active_set = set()
            for _, _, p in sorted_rotated_points:
                xp = points_with_index[p][0]
                xp_minus_yp = xp - points_with_index[p][1]
                points_to_remove = []
                for s in active_set:
                    xs = points_with_index[s][0]
                    xs_minus_ys = xs - points_with_index[s][1]
                    if xs <= xp and xp_minus_yp < xs_minus_ys:
                        edges.add(frozenset({s,p}))
                        points_to_remove.append(s)
                for s in points_to_remove:
                    active_set.discard(s)
                active_set.add(p)

            points_with_index = points_rotated_clockwise_45_degrees

        # apply Kruskal's Union Find algorithm to the graph of points with
        # the neighbor/adjacency list created above

        edges = [[mD(i,j), i, j] for (i,j) in edges]
        edges.sort()    # list of edges sorted in increasing order by distance

        # find
        def root(i: int) -> int:
            if parent[i] != i:
                parent[i] = root(parent[i])
            return parent[i]

        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]

        cost = 0
        unions = 0
        edge_index = 0
        while unions < n - 1:  # n-1 unions and they're all combined
            dist, u, v = edges[edge_index]
            edge_index += 1
            u, v = root(u), root(v)
            if u != v:
                unions += 1
                cost += dist
                # attach the smaller to the larger one
                if size[u] < size[v]:
                    parent[u] = v
                    size[v] += size[u]
                else:
                    parent[v] = u
                    size[u] += size[v]

        return cost

points=[[0,0],[2,2],[3,3],[2,4],[4,2]]
# points=[[0,0],[2,2],[3,10],[5,2],[7,0]]
print(Solution().minCostConnectPoints(points))