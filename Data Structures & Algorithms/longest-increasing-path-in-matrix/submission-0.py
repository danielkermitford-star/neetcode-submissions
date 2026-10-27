# https://neetcode.io/problems/longest-increasing-path-in-matrix/question?list=neetcode150
from collections import deque
from typing import List

# solve via memoization - calculate the longest path from a cell onward recursively
#   every time you get to a cell with a previously calculated value, i.e. the recursion
# has already explored all possible outgoing edges, you can use this value for this
# branch (without exploring it again) and explore the other branches.

# solve via DP - need an order to guarantee we have th best going forward - for this
# we need Kahn's Algorithm - explore all possible incoming paths and choose the longest
# one.  The DFS memoization algorithm above in reverse.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_rows = len(matrix)
        num_columns = len(matrix[0])

        queue = deque()

        in_degree = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
        for r in range(num_rows):
            for c in range(num_columns):
                for dr, dc in deltas:
                    nr = r + dr
                    nc = c + dc
                    if          0 <= nr < num_rows \
                            and 0 <= nc < num_columns \
                            and matrix[nr][nc] < matrix[r][c]:
                        in_degree[r][c] += 1
                if in_degree[r][c] == 0:
                    queue.append((r, c, 1))

        longest_path_to = [[1 for _ in range(num_columns)] for _ in range(num_rows)]
        max_path_length = 1
        while queue:
            (r, c, length_to) = queue.popleft()
            for dr, dc in deltas:
                nr = r + dr
                nc = c + dc
                if        0 <= nr < num_rows \
                        and 0 <= nc < num_columns \
                        and matrix[r][c] < matrix[nr][nc]:
                    in_degree[nr][nc] -= 1
                    longest_path_to[nr][nc] = max(longest_path_to[nr][nc], 1 + length_to)
                    if in_degree[nr][nc] == 0:
                        queue.append((nr, nc, longest_path_to[nr][nc]))
                        max_path_length = max(max_path_length, longest_path_to[nr][nc])

        return max_path_length

matrix = [[1,2,3],[2,1,4],[7,6,5]]
print(Solution().longestIncreasingPath(matrix))

