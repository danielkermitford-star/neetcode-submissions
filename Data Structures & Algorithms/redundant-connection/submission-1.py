# https://neetcode.io/problems/redundant-connection/question
from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors_of = [[] for _ in range(n+1)]
        for i, j in edges:
            neighbors_of[i].append(j)
            neighbors_of[j].append(i)

        for i, j in reversed(edges):
            stack = [i]
            seen = set()
            while stack:
                v = stack.pop()
                if v == j:
                    return [i, j]
                elif v in seen:
                    continue
                seen.add(v)
                for u in neighbors_of[v]:
                    if u != j or v != i:
                        stack.append(u)
        return []

edges=[[1,2],[1,3],[1,4],[3,4],[4,5]]
print(Solution().findRedundantConnection(edges))