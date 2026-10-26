# https://neetcode.io/problems/decode-ways/question?list=neetcode150

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        zero = ord('0')
        digit_at = [ord(c)-zero for c in s]

        if digit_at[0] == 0:
            return 0
        decodings = [1] * n

        for i in range(1,n):
            d = digit_at[i]
            n = 10 * digit_at[i-1] + d
            if n == 0:
                return 0
            if d == 0:
                if n >= 30:
                    return 0
                decodings[i] = decodings[i-2] # n in {10, 20}
                decodings[i-1] = 0
            else: # d > 0
                decodings[i] = decodings[i-1]
                if n <= 26:
                    decodings[i] += decodings[i-2]

        return decodings[-1]

s = "12"
s = "01"
s="226"
s="2101"
s="10011"
s="207"
print(Solution().numDecodings(s))