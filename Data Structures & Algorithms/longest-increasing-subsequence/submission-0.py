# https://neetcode.io/problems/longest-increasing-subsequence/question?list=neetcode150
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1 for _ in range(len(nums))]
        for i,n in enumerate(nums):
            lis[i] = 1+ max([lis[j] for j in range(i) if nums[j] < nums[i]], default=0)

        return max(lis)

nums = [9,1,4,2,3,3,7]
print(Solution().lengthOfLIS(nums))