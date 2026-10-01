from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # triplets = []
        t_set = set()
        nums.sort() # need to keep duplicates, e.g. (-2, 1, 1)
        for i, n in enumerate(nums):
            mid = i + 1
            right = len(nums) - 1
            while (mid < right):
                sum = n + nums[mid] + nums[right]
                if sum == 0:
                    if ((n, nums[mid]) not in t_set):
                        t_set.add((n, nums[mid]))
                        # triplets.append([n, nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                elif sum < 0:
                    mid += 1
                else:
                    right -= 1

        # return triplets
        return [[a,b,-(a+b)] for a,b in t_set]

nums=[-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))