# https://neetcode.io/problems/word-break/question?list=neetcode150
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=len)

        segmentable = [False] * (len(s))
        for i in range(len(s)):
            for word in wordDict:
                word_length = len(word)
                if i + 1 < word_length:
                    break           # words sorted by length - all subsequent word will be too long
                elif i + 1 == word_length:
                    if word == s[:i+1]:
                        segmentable[i] = True
                        break
                elif word == s[i+1-word_length:i+1] and segmentable[i-word_length]: # if the last letters in s up to i equal word
                    segmentable[i] = True
                    break

        print(segmentable)
        return segmentable[-1]


s="neetcode"
wordDict=["neet","code"]
# s="catsincars"
wordDict=["cats","cat","sin","in","car"]
s="dogs"
wordDict=["dog","s","gs"]
print(Solution().wordBreak(s, wordDict))