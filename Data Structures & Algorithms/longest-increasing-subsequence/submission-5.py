class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length_of_LIS_that_ends_at = [1] * len(nums)
        for i in range(1,len(nums)):
            max_length = 0
            for j in range (0,i):
                if (nums[j] < nums[i]):
                # if we found an index j < i such that
                #  nums[j] < nums[i] and
                #    it's bigger than any of the other one's
                #       we've found - then set it to max
                    if max_length < length_of_LIS_that_ends_at[j]:
                        max_length = length_of_LIS_that_ends_at[j]
            # end of the 'max_length' loop
            length_of_LIS_that_ends_at[i] = 1 + max_length
        
        # find the max in the array
        # max_lis = 1
        # for n in length_of_LIS_that_ends_at:
        #     if max_lis < n:
        #         max_lis = n
        
        # return max_lis
        return max(length_of_LIS_that_ends_at)