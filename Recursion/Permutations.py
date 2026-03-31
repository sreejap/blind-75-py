class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack (curr):
            if len (curr) == len (nums):
                res.append (list(curr)) # or res.append(curr[:])
            
            for n in nums:
                if n in curr: # check whether n exists in the list curr
                    continue
                curr.append (n)
                backtrack (curr)
                curr.pop()

        backtrack ([])
        return res
