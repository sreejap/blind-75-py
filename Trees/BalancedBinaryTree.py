# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity is O(n)
# This solution is O(n) because each node is visited exactly once in a single DFS traversal. At each node, I compute height and check balance in constant time. 
# I also short-circuit early if an unbalanced subtree is found. This avoids the naive O(n²) approach where heights are recomputed repeatedly
from typing import Tuple
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper (node:Optional[TreeNode]) -> Tuple [bool,int]:
            if not node:
                return True,-1
            
            leftBalanced, leftHeight = helper (node.left)
            if not leftBalanced:
                return False, 0
            
            rightBalanced, rightHeight = helper (node.right)
            if not rightBalanced:
                return False, 0
            
            return abs (leftHeight - rightHeight) < 2 , max (leftHeight, rightHeight) + 1

        
        return helper (root)[0]
        
