import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        neighbors_of = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            neighbors_of[a].append((p, b))          # prob of success
            neighbors_of[b].append((p, a))

        # print(neighbors_of)
        neg_prob_of_success = [0 for _ in range(n)]
        finalized = [False for _ in range(n)]
        heap = []
        # Python only has min heap, but we need a max heap, so use -prob_success (or prob of failure)
        heapq.heappush(heap, (-1, start_node))
        while heap:
            neqative_prob_success_to_node, node = heapq.heappop(heap)
            if not finalized[node]:
                finalized[node] = True
                if node == end_node:
                    return -neqative_prob_success_to_node
                for prob_success_to_neighbor, neighbor in neighbors_of[node]:
                    new_neg_prob_success = neqative_prob_success_to_node * prob_success_to_neighbor
                    if new_neg_prob_success < neg_prob_of_success[neighbor]:
                        neg_prob_of_success[neighbor] = new_neg_prob_success
                        heapq.heappush(heap, (new_neg_prob_success, neighbor))

        return 0

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
n=3
edges=[[0,1]]
succProb=[0.5]
start=0
end=2
res = Solution().maxProbability(n, edges, succProb, start, end)
print(res)

