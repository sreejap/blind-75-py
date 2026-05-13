# Because the problem is fundamentally about **nearest smaller elements**, not about repeatedly getting the “largest” or “smallest” bar globally.

# A **monotonic stack** preserves exactly the information you need:

# * bars in increasing height order
# * ability to quickly find:

#   * previous smaller bar
#   * next smaller bar

# A heap cannot efficiently give you that.

# ---

# # What the stack is actually doing

# For every bar, you want to know:

# * how far can this bar extend to the left
# * how far can this bar extend to the right
# * while still being the minimum height

# Area is:

# [
# \text{height} \times \text{width}
# ]

# The stack helps compute the width in **O(1)** amortized time.

# ---

# # Key insight

# When you encounter a shorter bar:

# ```python
# heights[i]
# ```

# you now know:

# > all taller bars before it must stop here

# So you pop them and calculate their areas.

# ---

# Example:

# ```python
# heights = [2,1,5,6,2,3]
# ```

# ---

# ## Stack evolution

# We store indices.

# ```python
# stack = [-1]
# ```

# ---

# ## i = 0, h = 2

# Push:

# ```python
# stack = [-1, 0]
# ```

# ---

# ## i = 1, h = 1

# Now:

# ```python
# heights[0] = 2 >= 1
# ```

# So bar `2` cannot continue past index 1.

# Pop it.

# ```python
# current_height = 2
# ```

# Width:

# ```python
# i - stack[-1] - 1
# = 1 - (-1) - 1
# = 1
# ```

# Area:

# ```python
# 2 * 1 = 2
# ```

# Then push 1.

# ---

# # Why a heap fails conceptually

# A heap gives you:

# * smallest element
#   OR
# * largest element

# But this problem needs:

# * nearest smaller element on LEFT
# * nearest smaller element on RIGHT

# A heap destroys positional structure.

# ---

# Example:

# Suppose:

# ```python
# [2,1,5,6,2,3]
# ```

# A heap might tell you:

# * smallest = 1

# But that tells you nothing about:

# * how far height 5 extends
# * where height 6 stops
# * neighboring boundaries

# You need **ordered boundaries**, not global priorities.

# ---

# # Why stack works perfectly

# The stack maintains:

# ```python
# increasing heights
# ```

# So when a smaller bar arrives:

# ```python
# while heights[stack[-1]] >= heights[i]:
# ```

# you immediately know:

# * current index = right boundary
# * new top of stack = left boundary

# That’s the whole trick.

# ---

# # Visual intuition

# The stack is basically remembering:

# > “These bars are still waiting to find their right boundary.”

# When a smaller bar appears:

# * it closes rectangles
# * areas are finalized

# A heap cannot model this “boundary discovery” efficiently.

# ---

# # Complexity comparison

# ## Stack solution

# Each index:

# * pushed once
# * popped once

# So:

# [
# O(n)
# ]

# ---

# ## Heap attempt

# You’d still need:

# * neighbor lookups
# * boundary tracking
# * deletions
# * interval management

# Likely becomes:

# [
# O(n \log n)
# ]

# or worse.

# ---

# # The deeper pattern

# Whenever a problem asks:

# * next greater
# * next smaller
# * span
# * nearest boundary
# * histogram
# * trapping rain water
# * temperatures

# think:

# > monotonic stack

# not heap.

# This is one of the most important interview patterns to internalize.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
      
        # Stack to maintain indices of bars in increasing height order
        stack = []
      
        # left[i] stores the index of the nearest smaller element to the left of i
        # Initialize to -1 (no smaller element on the left)
        left_boundaries = [-1] * n
      
        # right[i] stores the index of the nearest smaller element to the right of i
        # Initialize to n (no smaller element on the right)
        right_boundaries = [n] * n
      
        # Single pass to find both left and right boundaries
        for i, current_height in enumerate(heights):
            # Pop elements from stack that are >= current height
            # These elements have found their right boundary (current index)
            while stack and heights[stack[-1]] >= current_height:
                right_boundaries[stack[-1]] = i
                stack.pop()
          
            # The remaining top of stack (if exists) is the left boundary for current element
            if stack:
                left_boundaries[i] = stack[-1]
          
            # Add current index to stack
            stack.append(i)
      
        # Calculate maximum rectangle area
        # For each bar, the rectangle width is (right_boundary - left_boundary - 1)
        # and height is the bar's height
        max_area = max(
            height * (right_boundaries[i] - left_boundaries[i] - 1) 
            for i, height in enumerate(heights)
        )
      
        return max_area
