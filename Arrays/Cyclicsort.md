# Cycle sort is a sorting algorithm that can sort a given sequence in a range from a to n by putting each element at the index that corresponds to its value.

# nums is a zero-indexed array, so an element with the value x will be located at index x - 1. For example, 1 goes at index 0 in the array, 2 goes at index 1, and 100 goes at index 99.

# For each element x in nums, if it is a positive integer between 1 and n, we place it at index nums[x - 1]. Elements smaller than 1 or larger than n will reside at indexes that do not have a corresponding value in nums.

# Then, to determine the smallest positive integer, we iterate through nums, and return the first element that is not equal to its index plus one.


# to do - https://leetcode.com/problems/first-missing-positive/editorial/
