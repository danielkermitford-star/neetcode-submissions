from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        # t_set = set() # check if triplets already seen
        # left < mid < right so duplicates must consist of adjacent numbers
        # and we don't need to use a set
        nums.sort()
        left = 0
        while left < len(nums) -2:
            n0 = nums[left]
        # for left, n0 in enumerate(nums[:-2]):
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                n1 = nums[mid]
                n2 = nums[right]
                sum = n0 + n1 + n2
                if sum == 0:
                    # if ((n, n1, n2) not in t_set):
                        # t_set.add((n, n1, n2))
                        # triplets.append([n, nums[mid], nums[right]])
                    triplets.append([n0, n1, n2])
                    while mid < right and nums[mid] == n1:
                        mid += 1
                    while mid < right and nums[right] == n2:
                        right -= 1
                    # mid += 1
                    # right -= 1
                elif sum < 0:
                    mid += 1
                else:
                    right -= 1
            while left < len(nums) - 2 and nums[left] == n0:
                left += 1

        return triplets

nums=[-1,0,1,2,-1,-4]
nums=[0,0,0,0]
print(Solution().threeSum(nums))