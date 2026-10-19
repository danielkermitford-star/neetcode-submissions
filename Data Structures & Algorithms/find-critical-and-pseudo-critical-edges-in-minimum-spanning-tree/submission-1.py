# https://neetcode.io/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/question?list=neetcode150
from cmath import inf
from enum import nonmember
from typing import List, Set


class Solution:
    # returns inf if no MST exists
    def MST_weight(self, n: int, sorted_edges: List[List[int]], critical_edge: int, pseudo_critical_edge: List[int]) -> int:
        size_of = [1 for _ in range(n)]
        parent_of = [v for v in range(n)]

        # returns the root of the tree containing the argument, u.
        # optimization path-compression:
        # makes every node in the path from u to the root a child of root
        # reduces the path length to the root for every node in these branches
        # making it quicker to find them in the future
        def find_root(u) -> int:
            path_to_root = [u]
            while u != parent_of[u]:
                u = parent_of[u]
                path_to_root.append(u)
            root = u
            for v in path_to_root:
                parent_of[v] = root
            return root

        # joins the trees containing t and u
        # returns TRUE if the trees were joined and FALSE if t and u were already in the same tree
        # optimization:
        # finds the roots of their trees and makes the root of the smaller one
        # a child of the root of the larger one
        def union(t, u) -> bool:
            root1, root2 = find_root(u), find_root(t)
            if root1 != root2:
                if size_of[root1] < size_of[root2]:
                    parent_of[root1] = root2
                    size_of[root2] += size_of[root1]
                else:
                    parent_of[root2] = root1
                    size_of[root1] += size_of[root1]
                return True
            return False

        number_of_connected_components = n
        weight_of_MST = 0
        if pseudo_critical_edge:
            u, v, w = pseudo_critical_edge
            union(u, v)
            weight_of_MST += w
            number_of_connected_components -= 1

        for w, i, u, v in sorted_edges:
            # skip any critical edge then only add the edge if vertices, (a,b), weren't already in the same tree
            if critical_edge != i and union(u, v):
                weight_of_MST += w
                number_of_connected_components -= 1
                if number_of_connected_components == 1:
                    return weight_of_MST  # found MST - no more components/trees to join
        return inf

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        sorted_edges = sorted([(w,i,u,v) for i,(u,v,w) in enumerate(edges)])

        # sorted_edges = sorted(edges_with_index)
        weight_of_MST = self.MST_weight(n, sorted_edges, None, None)


        critical_edge_indices = []
        edge_index_range = range(len(edges))
        noncritical_edge_indices = set(edge_index_range)
        for i in edge_index_range:
            if self.MST_weight(n, sorted_edges, i, None) > weight_of_MST:
                critical_edge_indices.append(i)
                noncritical_edge_indices.remove(i)

        pseudo_critical_edge_indices = []
        for i in noncritical_edge_indices:
            if self.MST_weight(n, sorted_edges, None, edges[i]) == weight_of_MST:
                pseudo_critical_edge_indices.append(i)

        return [critical_edge_indices, pseudo_critical_edge_indices]

n = 4
edges = [[0,3,2],[0,2,5],[1,2,4]]
n=5
edges=[[0,3,2],[0,4,2],[1,3,2],[3,4,2],[2,3,1],[1,2,3],[0,1,1]]
print(Solution().findCriticalAndPseudoCriticalEdges(n, edges))

