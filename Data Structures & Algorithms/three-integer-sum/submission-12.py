from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        t_set = set()
        nums.sort()
        for i, n in enumerate(nums):
            mid = i + 1
            right = len(nums) - 1
            while (mid < right):
                sum = n + nums[mid] + nums[right]
                if sum == 0:
                    if ((n, nums[mid], nums[right]) not in t_set):
                        t_set.add((n, nums[mid], nums[right]))
                        triplets.append([n, nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                elif sum < 0:
                    mid += 1
                else:
                    right -= 1

        return triplets

nums=[-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))