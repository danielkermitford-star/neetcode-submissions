# https://neetcode.io/problems/house-robber-ii/question?list=neetcode150
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # the total if robbing house i <= 1 is nums[i]
        max_do = nums.copy()                # max if you rob house i == 0
        max_dont = [0 for _ in range(n)]    # max if you don't rob house i == 0

        max_do_skip_0 = [0 for _ in range(n)]     # max if you rob house i (but skip 0)
        max_dont_skip_0 = [0 for _ in range(n)]   # max if you don't rob house i == 0 (but skip 0)

        for i in range(1, n-1):
            max_do[i] = nums[i] + max_dont[i - 1]
            max_dont[i] = max(max_do[i-1], max_dont[i - 1])
            max_do_skip_0[i] = nums[i] + max_dont_skip_0[i - 1]
            max_dont_skip_0[i] = max(max_do_skip_0[i - 1], max_dont_skip_0[i - 1])

        # you can only rob the last house if you neither rob the second to last, nor the first
        max_do[n-1] = nums[n-1] + max_dont_skip_0[n-2]
        max_dont[n-1] = max(max_do[n-2], max_dont[n - 2])

        return max(max_do[n-1], max_dont[n-1])


nums = [2,9,8,3,6]
print(Solution().rob(nums))