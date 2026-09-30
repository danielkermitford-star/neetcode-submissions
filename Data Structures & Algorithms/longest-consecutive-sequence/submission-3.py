class Solution:
    # classic DP problem
    # Let LCS(n) be the length of the LCS ending with 
    # the current value, n.
    # LCS(n) = 1 if n-1 is not left of n in the list
    # LCS(n) = 1 + LCS(n-1) otherwise
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = {}
        if not nums:
            return 0
        for n in sorted(nums):
            lcs[n] = 1 + lcs.get(n - 1, 0)
        return max(lcs.values())
        