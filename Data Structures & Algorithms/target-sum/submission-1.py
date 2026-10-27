# https://neetcode.io/problems/target-sum/question?list=neetcode150
from collections import Counter
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        counts = [Counter() for _ in range(len(nums)+1)]
        counts[0][0] = 1
        for i,num in enumerate(nums):
            for key,val in counts[i].items():
                counts[i+1][key - num] += val
                counts[i+1][key + num] += val
            # print(counts)
        return counts[len(nums)][target]

nums = [2,2,2]
target = 2
print(Solution().findTargetSumWays(nums, target))
