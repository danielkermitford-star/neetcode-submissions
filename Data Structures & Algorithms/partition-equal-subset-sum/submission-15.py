# https://neetcode.io/problems/partition-equal-subset-sum/question?list=neetcode150

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half_total = total // 2
        subset_sums = set([0]) # the possible subset sums using elements before
        for num in nums:
            subset_sums = subset_sums | set([n + num for n in subset_sums if n+num <= half_total])
        if half_total in subset_sums:
            return True
        return False
        # return half_total in subset_sums
