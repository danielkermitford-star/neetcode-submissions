class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2  # truncates remainder
            # left + 1 = right => 
            # (right + left) // 2 = (2*left + 1) // 2 = left 
            if nums[mid] < nums[right]:
                right = mid          # minimum at mid or left of it
            elif nums[mid] > nums[right]:
                left = mid + 1
            else: # nums[mid] = nums[right] => left == right
                return nums[mid]
        return nums[0]  # error