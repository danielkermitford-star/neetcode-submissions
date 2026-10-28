# https://neetcode.io/problems/regular-expression-matching/question?list=neetcode150

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matches = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            matches[i][0] = False   # en empty pattern can only match the empty string
        matches[0][0] = True
        for i in range(2, len(p) + 1, 2):
            if p[i-1] == '*':
                matches[0][i] = matches[0][i - 2]
            else:
                break
        # an empty string can only be matched by an empty pattern or anything followed by a *
        # a * must be preceded by a . or a valid character: a lower case english letter

        for pi in range(len(p)):
            si = 1
            for si in range(len(s)):
                if p[pi] == '*':
                    if pi > 0 and matches[si+1][pi-1]:
                        matches[si+1][pi+1] = True
                    else:
                        for i in range(si,-1,-1):
                            if pi > 0 and p[pi-1] not in ['.', s[i]]:
                                break;
                            elif matches[i+1][pi]:
                                matches[si+1][pi+1] = True
                                break;
                elif p[pi] in ['.', s[si]] and matches[si][pi]:
                    matches[si+1][pi+1] = True
        print(*matches, sep='\n')
        return matches[-1][-1]
        return True

s = "aa"
p = ".b"
s="aab"
p="c*a*b"
# s="aaa"
# p="ab*ac*a"
s="a"
p="ab*"
s="nnn"
p="n*"
print(Solution().isMatch(s, p))