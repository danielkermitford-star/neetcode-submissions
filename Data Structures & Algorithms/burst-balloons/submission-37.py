# https://neetcode.io/problems/burst-balloons/question?list=neetcode150

# Google AI optimized version

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 1. Compress the state space by filtering out zeros
        nums = [x for x in nums if x > 0]
        coins = [1] + nums + [1]
        n = len(coins)

        # 2. Maintain two tables: standard and transposed
        value = [[0] * n for _ in range(n)]
        value_T = [[0] * n for _ in range(n)]

        # 3. Outer loop moves the left boundary backwards
        for l in range(n - 3, -1, -1):
            l_row = value[l]  # Direct 1D reference to the left row

            # 4. Middle loop moves the right boundary forwards
            for r in range(l + 2, n):
                r_row_T = value_T[r]  # Direct 1D reference to the right column (as a row)

                outer_product = coins[l] * coins[r]
                max_value = 0

                # 5. Tight Innermost Loop: Zero 2D pointer hops, zero index arithmetic!
                for i in range(l + 1, r):
                    ith_value = coins[i] * outer_product + l_row[i] + r_row_T[i]
                    if ith_value > max_value:
                        max_value = ith_value

                # Sync the result to both tables
                l_row[r] = max_value
                r_row_T[l] = max_value

        # The full range of elements spans from index 0 to n-1 (exclusive)
        return value[0][n - 1]

nums = [4,2,3,7]
print(Solution().maxCoins(nums))