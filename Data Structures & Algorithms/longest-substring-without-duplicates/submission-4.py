class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxstr = 0
        start = -1
        for i, c in enumerate(s):
            if c in seen:
                start = max(start, seen[c])
            seen[c] = i
            maxstr = max(maxstr, i - start)
        return maxstr