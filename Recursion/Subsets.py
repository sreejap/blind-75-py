class Solution:
    # That “expand → explore → backtrack” pattern is the core of backtracking.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums) == 0:
            return [[]]
        
        def helper (index, path):            
            res.append(path[:]) # every node is a valid answer for subsets, make a copy
            for i in range (index,len(nums)):
                path.append (nums[i])
                helper (i+1, path)
                path.pop() # removes the last element
            
        helper (0,[])
        return res
