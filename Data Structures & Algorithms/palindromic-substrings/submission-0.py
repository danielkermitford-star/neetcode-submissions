# https://neetcode.io/problems/palindromic-substrings/question?list=neetcode150
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome_indices = [[] for i in range(n)]
        palindrome_indices[0] = [0]
        for i in range(1, n):
            for j in palindrome_indices[i - 1]:
                if j > 0 and s[j - 1] == s[i]:
                    palindrome_indices[i].append(j - 1)
            if (s[i] == s[i - 1]):
                palindrome_indices[i].append(i - 1)
            palindrome_indices[i].append(i)

        return sum(len(indices) for indices in palindrome_indices)

s = "abc"
s = "aaa"
print(Solution().countSubstrings(s))

