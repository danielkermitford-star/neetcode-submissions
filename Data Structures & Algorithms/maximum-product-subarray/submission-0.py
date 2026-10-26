# https://neetcode.io/problems/maximum-product-subarray/question?list=neetcode150
from cmath import inf
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_cur_prod = max_product = -inf
        min_cur_prod = inf
        for n in nums:
            if n >= 0:
                min_cur_prod, max_cur_prod = min(n, n * min_cur_prod), max(n, n * max_cur_prod)
            else:
                min_cur_prod, max_cur_prod = min(n, n * max_cur_prod), max(n, n * min_cur_prod)
            max_product = max(max_product, max_cur_prod)

        return max_product

nums = [-3,0,-2]
nums = [2,4,-3,5]
print(Solution().maxProduct(nums))

