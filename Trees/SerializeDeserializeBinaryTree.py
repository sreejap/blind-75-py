# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs (node):
            if not node:
                result.append ("None")
                return

            result.append (str(node.val)) # convert to string
            dfs (node.left)
            dfs (node.right)

        dfs (root)

        return ",".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = deque (data.split(','))
        def dfs ():
            if not nodes:
                return None
            
            val = nodes.popleft()
            
            if val == "None":
                return None

            node = TreeNode (int (val))
            node.left = dfs ()
            node.right = dfs ()
            return node
        
        root = dfs ()
        return root       

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
