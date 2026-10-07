# https://neetcode.io/problems/valid-tree/question?list=neetcode150
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # if len(edges) < n-1 graph is disconnected
        # if len(edges) > n-1 graph contains a cycle
        # if len(edges) == n-1 graph is either
        # disconnected with a cycle, or
        # connected with no cycle

        # so now we just return
        # True if it is connected and False otherwise

        neighbors_of = [[] for _ in range(n)]  # adjacency list
        for i, j in edges:
            neighbors_of[i].append(j)
            neighbors_of[j].append(i)

        # bfs - from any node, e.g. 0
        seen = set()
        current = set()
        current.add(0)
        while current:
            seen.update(current)
            unseen_neighbors = set()
            for vertex in current:
                for neighbor in neighbors_of[vertex]:
                    if neighbor not in seen:
                        unseen_neighbors.add(neighbor)
            current = set(unseen_neighbors)

        return len(seen) == n


n=5
edges=[[0,1],[0,2],[0,3],[1,4]]
print(Solution().validTree(n, edges))
