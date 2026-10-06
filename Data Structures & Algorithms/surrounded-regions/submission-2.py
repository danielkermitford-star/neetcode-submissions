from collections import deque
from typing import Set, Tuple, List


class Solution:
    def bfs(self, board: List[List[str]], can_escape: Set[Tuple[int, int]]) -> None:
        queue = deque(can_escape)
        can_escape.clear()
        while queue:
            i, j = queue.popleft()
            if (i, j) in can_escape or board[i][j] != 'O':
                continue
            else:
                can_escape.add((i, j))
            if i > 0:               queue.append((i - 1, j))
            if j > 0:               queue.append((i, j - 1))
            if i + 1 < len(board):    queue.append((i + 1, j))
            if j + 1 < len(board[0]): queue.append((i, j + 1))

    def solve(self, board: List[List[str]]) -> None:
        can_escape = set((i, j) for i, row in enumerate(board) for j, v in enumerate(row) if
                         (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1) and v == 'O')
        self.bfs(board, can_escape)

        captured = set((i, j) for i, row in enumerate(board) for j, _ in enumerate(row)) - can_escape

        for i, j in captured:
            board[i][j] = 'X'

board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)