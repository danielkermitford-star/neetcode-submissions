class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        sums = set([0])

        for num1 in nums:
            new_sums = []
            for num in sums:
                new_sums.append(num + num1)
                # if target in new_sums:
                #     return True
            for num in new_sums:
                sums.add(num)
            if target in sums:
                return True
        return False
