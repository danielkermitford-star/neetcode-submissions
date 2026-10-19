from cmath import inf
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ord_of_a = ord('a')

        def index_of(char):
            return ord(char) - ord_of_a

        # practice converting indices to letters and back
        letters = [chr(i + ord('a')) for i in range(26)]
        # print(letters)
        indices = [index_of(i) for i in letters]
        # print(indices)

        directed_edges = [(index_of(original[i]), index_of(changed[i]), cost[i]) for i in range(len(changed))]


        # Floyd-Warshall's Algorithm
        #initialize cost matrix
        cost_matrix = [[inf for _ in range(26)] for _ in range(26)]
        for i in range(26):
            cost_matrix[i][i] = 0

        for origin, destination, cost in directed_edges:
            cost_matrix[origin][destination] = min(cost_matrix[origin][destination], cost)

        # update distance when a shorter distance is found.
        for i in range(26):
            for origin in range(26):
                for destination in range(26):
                    cost_matrix[origin][destination] = min(cost_matrix[origin][destination], cost_matrix[origin][i] + cost_matrix[i][destination])

        total_cost = 0
        for origin, destination in zip(source, target):
            total_cost += cost_matrix[index_of(origin)][index_of(destination)]

        if total_cost != inf:
            return total_cost
        else:
            return -1


source="abcd"
target="acbe"
original=["a","b","c","c","e","d"]
changed=["b","c","b","e","b","e"]
cost=[2,5,5,1,2,20]
source="abcd"
target="abce"
original=["a"]
changed=["e"]
cost=[10000]
print(Solution().minimumCost(source, target, original, changed, cost))