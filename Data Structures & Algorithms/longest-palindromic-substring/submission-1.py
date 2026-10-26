# https://neetcode.io/problems/longest-palindromic-substring/question?list=neetcode150

class Solution:
    # map each index i to a list of indices, j, ending with i whose substring, substr(j,i+1), is a palindrome
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        palindrome_indices = [[] for i in range(n)]
        palindrome_indices[0] = [0]
        for i in range(1,n):
            for j in palindrome_indices[i-1]:
                if j > 0 and s[j-1] == s[i]:
                    palindrome_indices[i].append(j-1)
            if (s[i] == s[i-1]):
                palindrome_indices[i].append(i-1)
            palindrome_indices[i].append(i)

        k = n-1
        j = palindrome_indices[k][0]
        for m in range(0,n-1):
            l = palindrome_indices[m][0]
            if k - j < m - l :
                k, j = m, l

        return s[j:k+1]

s = "ababd"
s="abbc"
print(Solution().longestPalindrome(s))