class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix / postfix products from each end
        pre = [1]
        p = 1
        for n in nums:
            p *= n
            pre.append(p)

        post = [1]
        p = 1
        for n in nums[::-1]:
            p *= n
            post.append(p)
        post.reverse()

        output = []
        for i in range(len(nums)):
            output.append(pre[i] * post[i+1])
        
        return output
