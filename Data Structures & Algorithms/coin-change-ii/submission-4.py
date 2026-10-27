# https://neetcode.io/problems/coin-change-ii/question?list=neetcode150
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        num_ways = [0 for _ in range(amount + 1)]
        num_ways[0] = 1
        for coin in coins:
            for amount in range(1, amount + 1):
                if coin <= amount:
                   num_ways[amount] += num_ways[amount - coin]
        # print(*num_ways, sep='\n')
        return num_ways[-1]

amount = 4
coins = [1,2,3]
amount=0
coins=[7]
print(Solution().change(amount, coins))