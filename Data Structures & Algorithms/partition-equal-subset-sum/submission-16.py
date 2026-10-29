from typing import List
from collections import Counter

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        t = total >> 1
        if max(nums) > t:
            return False

        mask = (1 << (t + 1)) - 1
        bits = 1

        for v, k in Counter(nums).items():
            p = 1
            while k > 0:
                take = min(p, k)
                bits |= (bits << (v * take)) & mask
                k -= take
                p <<= 1
            if bits >> t & 1:
                return True

        return bool(bits >> t & 1)

nums=[1,2,3,4]
nums = [1,2,3,4,5]
print(Solution().canPartition(nums))