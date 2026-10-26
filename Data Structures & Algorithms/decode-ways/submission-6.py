# https://neetcode.io/problems/decode-ways/question?list=neetcode150

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        zero = ord('0')
        digit_at = [ord(c)-zero for c in s]
        n_ways_0_9 = [0 for _ in range(n)]      # num of ways where the last digit is treated by itself
        n_ways_10_26 = [0 for _ in range(n)]    # num of ways where the last two digits are combined
        if digit_at[0] == 0:
            return 0
        n_ways_0_9[0] = 1
        n_ways_10_26[0] = 0
        if n > 1:
            if digit_at[1] == 0:
                if digit_at[0] > 2:
                    return 0
                else: # 10 or 20
                    n_ways_0_9[0] = 0
                    n_ways_0_9[1] = 0
                    n_ways_10_26[1] = 1
            else: # 1 ... 9
                n_ways_0_9[1] = 1
                if (digit_at[0] == 2 and digit_at[1] >=7) or digit_at[0] >= 3:
                    n_ways_10_26[1] = 0
                else:
                    n_ways_10_26[1] = 1

        for i in range(2, n):
            if digit_at[i] == 0:
                if digit_at[i-1]  == 0 or digit_at[i-1] > 2:
                    return 0
                else:  # 10 or 20
                    n_ways_0_9[i] = 0
                    n_ways_0_9[i-1] = 0
                    n_ways_10_26[i-1] = 0
                    n_ways_10_26[i] = n_ways_0_9[i-2] + n_ways_10_26[i-2]
            else:  # 1 ... 9
                n_ways_0_9[i] = n_ways_0_9[i-1] + n_ways_10_26[i-1]
                if (digit_at[i-1] == 2 and digit_at[i] >= 7) or digit_at[i-1] >= 3:
                    n_ways_10_26[i] = 0
                else:
                    n_ways_10_26[i] = n_ways_0_9[i-2] + n_ways_10_26[i-2]

        return n_ways_0_9[-1] + n_ways_10_26[-1]

s = "12"
s = "01"
s="226"
s="2101"
s="10011"
s="207"
print(Solution().numDecodings(s))