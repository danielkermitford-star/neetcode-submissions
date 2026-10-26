# https://neetcode.io/problems/min-cost-climbing-stairs/question?list=neetcode150
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        total_cost = cost.copy()
        n = len(total_cost)
        # the cost of stepping off the i <= 1 step is cost[i]
        for i in range(2, n):
            total_cost[i] = cost[i] + min(total_cost[i - 1], total_cost[i - 2])
        return min(total_cost[n - 1], total_cost[n - 2])

cost=[1,2,3]
print(Solution().minCostClimbingStairs(cost))

