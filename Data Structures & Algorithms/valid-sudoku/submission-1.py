class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # test the rows
        for row in board:
            counts = Counter(row)
            mc = counts.most_common(2)
            if mc[0][0] != '.' and mc[0][1] > 1:
                return False
            elif len(mc) > 1 and mc[1][1] > 1:
                return False

        # test the columns
        for c in range(9):
            counts.clear()
            for r in range(9):
                counts.update(board[r][c])
            mc = counts.most_common(2)
            if mc[0][0] != '.' and mc[0][1] > 1:
                return False
            elif len(mc) > 1 and mc[1][1] > 1:
                return False

        # test the blocks
        counts = []
        for r in range(9):
            counts.append(Counter())

        for r in range(9):
            for c in range(9):
                square = (r // 3) * 3 + c // 3
                counts[square].update(board[r][c])
        for c in counts:
            mc = c.most_common(2)
            if mc[0][0] != '.' and mc[0][1] > 1:
                return False
            elif len(mc) > 1 and mc[1][1] > 1:
                return False
        return True