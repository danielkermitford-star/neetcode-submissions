# https://neetcode.io/problems/longest-common-subsequence/question?list=neetcode150

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1,l2 = len(text1), len(text2)
        lcs = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    lcs[i+1][j+1] = 1 + lcs[i][j]
                else:
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])

        print(*lcs, sep="\n")
        return lcs[-1][-1]

text1 = "cat"
text2 = "crabt"
text1="oxcpqrsvwf"
text2="shmtulqrypy"
print(Solution().longestCommonSubsequence(text1, text2))