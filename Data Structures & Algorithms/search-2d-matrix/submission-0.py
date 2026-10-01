class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1
        while left <= right:
            mid = (right + left) // 2  # truncates remainder
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            if value == target:
                return True
            # target can't be at mid
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False