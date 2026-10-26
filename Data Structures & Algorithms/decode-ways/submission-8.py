# https://neetcode.io/problems/decode-ways/question?list=neetcode150

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        decodings = [1] * n

        for i in range(1,n):
            d = s[i]
            n = int(s[i-1: i+1])
            if n == 0:
                return 0
            if d == '0':
                if n >= 30:
                    return 0
                decodings[i] = decodings[i-2] # n in {10, 20}
                decodings[i-1] = 0
            else: # d != '0'
                decodings[i] = decodings[i-1]
                if n <= 26:
                    decodings[i] += decodings[i-2]

        return decodings[-1]

s = "12"
print(Solution().numDecodings(s))