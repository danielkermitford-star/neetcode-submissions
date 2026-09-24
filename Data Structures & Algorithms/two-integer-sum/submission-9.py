class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = set()
        index = {}
        for i,n in enumerate(nums):
            if target - n in index:
                return [index[target - n], i]
            r.add(n)
            index[n] = i
