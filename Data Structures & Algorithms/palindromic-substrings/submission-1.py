# https://neetcode.io/problems/palindromic-substrings/question?list=neetcode150
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        at_indices = {}
        for i in range(n):
            at_indices.setdefault(s[i], []).append(i)
        palindrome = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            palindrome[i][i] = True
        count = n
        for end in range(0, n):
            for start in range(0, end):
                if s[start] != s[end]:
                    continue
                if start + 1 == end or palindrome[start+1][end-1]:
                    palindrome[start][end] = True
                    count += 1

        return count


s = "abc"
# s = "aaa"
print(Solution().countSubstrings(s))

