from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        while left < right - 1:
            while left < right - 1 and height[left] <= height[left + 1]:
                left += 1
                # either height[left] > height[left+1] or left == right - 1
            while left < right - 1 and height[right] <= height[right - 1]:
                right -= 1
                # either height[right] > height[right-1] or left == right - 1
            if left == right - 1:
                break
            elif height[left] <= height[right]:
                water_height = height[left]
                while (left < right and height[left] <= water_height):
                    water += water_height - height[left]
                    left += 1
            elif height[left] > height[right]:
                water_height = height[right]
                while (left < right and height[right] <= water_height):
                    water += water_height - height[right]
                    right -= 1
        return water

height=[0,2,0,3,1,0,1,3,2,1]
height=[4,2,0,3,2,5]
print(Solution().trap(height))