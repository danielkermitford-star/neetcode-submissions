from typing import List


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
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # nums[mid] < nums[left] => nums[mid] < nums[right]
            # elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

nums = [3,4,5,6,1,2]
target = 1
print(Solution().search(nums, target))