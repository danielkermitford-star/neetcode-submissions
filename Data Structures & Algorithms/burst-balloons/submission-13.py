# https://neetcode.io/problems/burst-balloons/question?list=neetcode150
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        coins = [1] + nums + [1]
        value = {}

        def findMaxValue(l: int, r: int) -> int:
            if (l,r) in value:
                return value[(l,r)]
            if l > r:
                return 0
            if l == r:
                return coins[l - 1] * coins[l] * coins[l + 1]
            max_value = 0
            for i in range(l, r + 1):
                ith_value = coins[l-1] * coins[i] * coins[r + 1]
                ith_value += findMaxValue(l, i-1)
                ith_value += findMaxValue(i+1, r)
                max_value = max(max_value, ith_value)
            value[(l, r)] = max_value
            return max_value

        result = findMaxValue(1, len(nums))
        # print(coins)
        # print(value)
        return result



nums = [4,2,3,7]
print(Solution().maxCoins(nums))