# https://www.youtube.com/watch?v=k7lrTYsFsHI
from typing import List
class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        arr = heights + [0] # creates an artificial final bar that is shorter than every real bar (assuming heights are non-negative). When the loop reaches this 0, it forces the while:
        # to pop all remaining bars and computing the areas
        stack = []
        mx = 0

        for i, h in enumerate(arr):
            while stack and arr[stack[-1]] > h:
                H = arr[stack.pop()]
                if not stack:
                    W = i
                else:
                    W = i - stack[-1] -1
                mx = max(mx, H * W)
            stack.append(i)

        return mx
