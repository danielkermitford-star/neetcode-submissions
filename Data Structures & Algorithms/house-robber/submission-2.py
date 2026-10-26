# https://neetcode.io/problems/house-robber/question?list=neetcode150
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # the total if robbing house i <= 1 is nums[i]
        max_do = nums.copy()                # max if you rob house i == 0
        max_dont = [0 for _ in range(n)]    # max if you don't rob house i == 0
        for i in range(1, n):
            max_do[i] = nums[i] + max_dont[i - 1]
            max_dont[i] = max(max_do[i-1], max_dont[i - 1])

        return max(max_dont[n-1], max_do[n-1])

nums=[1,1,3,3]
print(Solution().rob(nums))
