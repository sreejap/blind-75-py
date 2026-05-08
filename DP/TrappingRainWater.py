# https://algo.monster/liteproblems/42
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len (height)

        total_water = 0

        left = [0] * n
        right = [0] * n

        left[0] = height [0]
        right[n-1] = height [n-1]

        for i in range (1,n):
            left[i] = max (left[i-1], height[i]) # find max height from left

        for i in range (n-2, -1, -1):
            right [i] = max (right[i+1],height[i]) # find max height from right

        for i in range (n):
            min_water_height = min (left[i],right[i]) # find the water that could be held
            water_level = min_water_height - height[i] # subtract height of tower to get the water trapped

            total_water += water_level

        return total_water
