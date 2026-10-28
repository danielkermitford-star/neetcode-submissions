# https://neetcode.io/problems/burst-balloons/question?list=neetcode150

# Google AI optimized version

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # 1. Filter out zeros instantly
        nums = [x for x in nums if x > 0]
        if not nums: return 0

        coins = [1] + nums + [1]
        n = len(coins)

        # 2. Flatten the 2D grid into a single contiguous 1D array
        # This forces Python to use a single block of sequential memory
        dp = [0] * (n * n)

        # 3. Cache the list read method directly to a local variable
        # This forces the CPython interpreter to use its fastest internal LOAD_FAST bytecode
        coins_i = coins.__getitem__

        for length in range(2, n):
            for l in range(0, n - length):
                r = l + length
                outer_product = coins_i(l) * coins_i(r)

                # Deduce the flat 1D coordinates
                row_offset = l * n
                dp_idx = row_offset + r

                max_val = 0
                # Fast inner lookup using the single flat block
                for i in range(l + 1, r):
                    ith_val = coins_i(i) * outer_product + dp[row_offset + i] + dp[i * n + r]
                    if ith_val > max_val:
                        max_val = ith_val

                dp[dp_idx] = max_val

        return dp[n - 1]


nums = [4,2,3,7]
print(Solution().maxCoins(nums))