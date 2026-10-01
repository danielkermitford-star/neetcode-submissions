class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2  # truncates remainder
            # left + 1 = right => 
            # (right + left) // 2 = (2*left + 1) // 2 = left 
            if nums[mid] == target:
                return mid
            # target can't be at mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
