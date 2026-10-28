# https://neetcode.io/problems/burst-balloons/question?list=neetcode150
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [1] + nums + [1]
        n = len(coins)
        # value = {}
        value = [[0] * n for _ in range(len(coins))]

        def findMaxValue(l: int, r: int) -> int:
            if value[l][r] != 0:
                return value[l][r]
            # if l > r:
            #     return 0
            if l == r:
                return coins[l - 1] * coins[l] * coins[l + 1]
            max_value = 0
            outside_product = coins[l - 1] * coins[r + 1]
            for i in range(l, r + 1):
                ith_value = coins[i] * outside_product
                if (l <= i-1):
                    ith_value += findMaxValue(l, i-1)
                if (i+1 <= r):
                    ith_value += findMaxValue(i+1, r)
                if ith_value > max_value:
                    max_value = ith_value
                # max_value = max(max_value, ith_value)
            value[l][r] = max_value
            return max_value

        result = findMaxValue(1, len(nums))
        # print(coins)
        # print(value)
        return result



nums = [4,2,3,7]
print(Solution().maxCoins(nums))