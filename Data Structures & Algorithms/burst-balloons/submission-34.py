# https://neetcode.io/problems/burst-balloons/question?list=neetcode150
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [i for i in nums if i > 0]
        coins = [1] + nums + [1]
        n = len(coins)

        value = [[0] * n for _ in range(n)]

        # base case - length/range of 1 single element
        for i in range(1, n-1):
            value[i][i] = coins[i-1] * coins[i] * coins[i+1]

        for length in range(1, n-1):
            for l in range(1, n-length):
                l_row_value = value[l]
                r = l + length - 1
                max_value = 0
                outer_product = coins[l-1] * coins[r+1]
                for i in range(l, r+1):
                    # ith_value = coins[i] * outer_product
                    # if l <= i-1:
                    # ith_value += value[l][i-1]
                    # ith_value += l_row_value[i - 1]
                    # if i+1 <= r:
                    # ith_value += value[i+1][r]
                    ith_value = coins[i] * outer_product + l_row_value[i-1] + value[i+1][r]
                    if ith_value > max_value:
                        max_value = ith_value
                    # max_value = max(max_value, ith_value)
                value[l][r] = max_value

        # print(*value, sep='\n')
        return value[1][n-2]


nums = [4,2,3,7]
print(Solution().maxCoins(nums))