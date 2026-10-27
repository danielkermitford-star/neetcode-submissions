# https://neetcode.io/problems/edit-distance/question?list=neetcode150

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        edit_distance = [[i+j for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    edit_distance[i+1][j+1] = edit_distance[i][j]
                else:
                    edit_distance[i+1][j+1] = 1 + min(edit_distance[i+1][j], edit_distance[i][j+1], edit_distance[i][j])
        return edit_distance[-1][-1]

word1="monkeys"
word2="money"
word1="neatcdee"
word2="neetcode"
print(Solution().minDistance(word1,word2))