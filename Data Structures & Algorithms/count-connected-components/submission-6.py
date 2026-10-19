# https://neetcode.io/problems/count-connected-components/question
from typing import List, Set


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent_of = [v for v in range(n)]
        size_of = [1 for _ in range(n)]

        # return root of tree containing u
        # to make find as fast as possible we want the tree as wide as possible
        # so we make all the nodes in the path up to the root direct children
        # of the root
        def find(u) -> int:
            path = []
            while u != parent_of[u]:
                path.append(u)
                u = parent_of[u]
            root = u
            for n in path:
                parent_of[n] = root
            return root

        # join trees containing t and u - unless they are already in the same tree
        # to make find as fast as possible we want the tree as flaat/wide as possible
        # make the root of the smaller tree a child of the root of the larger tree
        # the size of the larger tree has now increased by the size of the smaller tree
        def union(t, u):
            root_of_t, root_of_u = find(t), find(u)
            if root_of_t != root_of_u:
                if size_of[root_of_t] < size_of[root_of_u]:
                    parent_of[root_of_t] = root_of_u
                    size_of[root_of_u] += size_of[root_of_t]
                else: # size_of[root_of_t] >= size_of[root_of_u]
                    parent_of[root_of_u] = root_of_t
                    size_of[root_of_t] += size_of[root_of_u]
                return True
            return False

        number_of_connected_components = n
        for u,v in sorted(edges):
            if union(u, v):
                number_of_connected_components -= 1

        return number_of_connected_components

n = 5
edges = [[0,1],[1,2],[3,4]]
print(Solution().countComponents(n, edges))

