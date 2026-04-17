# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def array_to_tree (left,right):
            nonlocal preorder_index

            if left > right:
                return None
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = TreeNode (root_val)
            root.left = array_to_tree (left,inorder_index_map[root_val] - 1)
            root.right = array_to_tree (inorder_index_map[root_val]+1,right)
            return root

        preorder_index = 0    
        inorder_index_map = {}
        for index, val in enumerate(inorder):
            inorder_index_map [val] = index
        
        root_node = array_to_tree (0,len(preorder)-1)
        return root_node        
