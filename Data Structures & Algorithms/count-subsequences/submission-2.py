# https://neetcode.io/problems/count-subsequences/question?list=neetcode150

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        count = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            count[i][0] = 1
        for si in range(1, len(s) + 1):
            for ti in range(1, len(t) + 1):
                count[si][ti] = count[si-1][ti]         # don't use the letter
                if s[si-1] == t[ti-1]:                  # if the letter matches
                    count[si][ti] += count[si-1][ti-1]  # use the letter
        print(*count, sep='\n')
        return count[-1][-1]

s = "caaat"
t = "cat"
print(Solution().numDistinct(s, t))