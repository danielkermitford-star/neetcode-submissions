# https://neetcode.io/problems/valid-tree/question?list=neetcode150
from collections import deque
from typing import List

# hint a tree is a connected graph with exactly n-1 edges.
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        neighbors_of = [[] for _ in range(n)]  # adjacency list
        for i, j in edges:
            neighbors_of[i].append(j)
            neighbors_of[j].append(i)

        return self.bfs_n_connected_vertices2(neighbors_of) == n

    def bfs_n_connected_vertices(self, neighbors_of: list[list[int]]) -> int:
        # bfs - from 0 as you know it always exists
        seen = set()
        current = set()
        current.add(0)
        while current:
            seen.update(current)
            unseen_neighbors_of_current = set()
            for vertex in current:
                for neighbor in neighbors_of[vertex]:
                    if neighbor not in seen:
                        unseen_neighbors_of_current.add(neighbor)
            current = set(unseen_neighbors_of_current)
        return len(seen)

    def bfs_n_connected_vertices2(self, neighbors_of: list[list[int]]) -> int:
        # bfs - from 0 as you know it always exists
        seen = set()
        queue = deque([0])
        while queue:
            v = queue.popleft()
            if v in seen:
                continue
            seen.add(v)
            for neighbor in neighbors_of[v]:
                queue.append(neighbor)

        return len(seen)



n=5
edges=[[0,1],[0,2],[0,3],[1,4]]
print(Solution().validTree(n, edges))
