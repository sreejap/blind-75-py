# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
# T(C) - o(N)
# S(C) - O(D) to keep the queues, where D is a tree diameter. 
# Let's use the last level to estimate the queue size. This level could contain up to N/2 tree nodes in the case of complete binary tree.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we will do a bfs and add the nodes to the queue
        # the ones at the end using the pop method are the ones for
        # right side view
        
        if not root:
            return []
        queue = deque ([root])
        res = []
        while queue:
            level_length = len (queue)
            for i in range (level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                if i == level_length-1:
                    res.append(node.val)
        return res        
