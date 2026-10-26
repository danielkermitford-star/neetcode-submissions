# https://neetcode.io/problems/count-paths/question?list=neetcode150

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        number_of_ways = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                number_of_ways[i][j] = number_of_ways[i-1][j] + number_of_ways[i][j-1]

        return number_of_ways[-1][-1]


m=3
n=6
n=3
print(Solution().uniquePaths(m,n))