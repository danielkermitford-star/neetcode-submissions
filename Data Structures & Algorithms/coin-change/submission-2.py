# https://neetcode.io/problems/coin-change/question?list=neetcode150
from cmath import inf
from typing import List


class Solution:
    # fewest # of coins
    def coinChange(self, coins: List[int], amount: int) -> int:
        n_coins = [0 for _ in range(amount + 1)]
        for n in range(1, amount + 1):
            count = inf     # inf means impossible
            for coin in coins:
                if n - coin >= 0:
                    count = min(count, n_coins[n - coin] + 1)
            n_coins[n] = count

        return n_coins[amount] if n_coins[amount] != inf else -1

coins=[1,2,5]
amount=11
print(Solution().coinChange(coins, amount))