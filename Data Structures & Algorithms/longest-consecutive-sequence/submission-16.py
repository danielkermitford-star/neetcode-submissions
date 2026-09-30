class Solution:
    # classic DP problem if the order mattered
    # Let LCS(n) be the length of the LCS ending with 
    # the current value, n.
    # LCS(n) = 1 if n-1 is not left of n in the list
    # LCS(n) = 1 + LCS(n-1) otherwise
    # Since it doesn't you could sort it, but this takes O(nlgn)

    # you could create linked lists of consecutive elements
    # or just keep track of the consecutive ranges of numbers

    # def longestConsecutive(self, nums: List[int]) -> int:
    #     lcs = {}
    #     if not nums:
    #         return 0
    #     for n in sorted(nums):
    #         lcs[n] = 1 + lcs.get(n - 1, 0)
    #     return max(lcs.values())

    def longestConsecutive(self, nums: List[int]) -> int:
        i = {}  # map from start to end of sequence
        d = {}  # map from end to start of sequence
        for n in set(nums):
            if n-1 in d and n+1 in i:
                s = d[n-1]
                e = i[n+1]
                i[s] = e
                d[e] = s
                del d[n-1]
                del i[n+1]
            elif n+1 in i:
                e = i[n+1]
                i[n] = e
                d[e] = n
                del i[n+1]
            elif n-1 in d:
                s = d[n-1]
                d[n] = s
                i[s] = n
                del d[n-1]
            elif n not in d and n not in i:
                i[n] = n
                d[n] = n

        lcs = 0
        for k,v in i.items():
            if lcs < v + 1 - k:
                lcs = v + 1 - k
            # lcs = max(lcs, v+1-k)
        
        return lcs
            