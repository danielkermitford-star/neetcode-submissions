class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the height of the rectangle is the height of one of the bars
        # for each bar height determine the number of sequential bars 
        # before and after it with the same height. => O(n^2)
        # unless we use an increasing stack of heights of each rectangle
        # seen so far. If the current height is less than the last item on 
        # the stack, then it is the right limit for that height/rectangle
        # and similarly for all the heights on the stack larger
        # than it.  After removing them the current height is, at least as 
        # high as the height on the top of the stack - if it's the same, do
        # nothing. If it's taller then add it to the stack with the previous
        # top as the left bound. 
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                right[stack[-1]] = i
                stack.pop()
            if stack:
                if heights[stack[-1]] == h:
                    left[i] = left[stack[-1]]
                else:
                    left[i] = stack[-1]
            stack.append(i)

        return max(heights[i] * (right[i] - left[i] - 1) for i in range(n))
                