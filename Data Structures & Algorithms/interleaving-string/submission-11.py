# https://neetcode.io/problems/interleaving-string/question?list=neetcode150

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        can_interleave = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        can_interleave[0][0] = True
        for i1 in range(len(s1)):
            if s1[i1] == s3[i1]:
                can_interleave[i1+1][0] = True
            else:
                break
        for i2 in range(len(s2)):
            if s2[i2] == s3[i2]:
                can_interleave[0][i2+1] = True
            else:
                break

        for i1 in range(len(s1)):
            for i2 in range(len(s2)):
                if can_interleave[i1][i2+1]:
                    if s1[i1] == s3[1+i1+i2]:
                        can_interleave[i1+1][i2+1] = True
                elif can_interleave[i1+1][i2]:
                     if s2[i2] == s3[1+i1+i2]:
                        can_interleave[i1+1][i2+1] = True
        print(*can_interleave,sep='\n')
        return can_interleave[-1][-1]


s1="aaaa"
s2="bbbb"
s3="aabbbbaa"
s1 = "abc"
s2 = "xyz"
s3 = "abxzcy"
s1="aabcc"
s2="dbbca"
s3="aadbbcbcac"
s1="db"
s2="b"
s3="cbb"
# print(Solution().isInterleave(s1,s2,s3))
