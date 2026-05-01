# https://leetcode.com/problems/minimum-height-trees/
# Let ∣V∣ be the number of nodes in the graph, T(C) - O(|V|), S(C) - O(|V|) 
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return [i for i in range (n)]
        
        leaves = []
        neighbors = [set() for i in range (n)]

        for start,end in edges:
            neighbors[start].add(end) # there is no append for set
            neighbors[end].add(start)
        
        for i in range (n):
            if len(neighbors[i]) == 1:
                leaves.append (i)
        
        remaining_nodes = n

        while remaining_nodes > 2: # we assume there will be atmost 2
            remaining_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()
                n1 = neighbors[leaf].pop()
                neighbors[n1].remove (leaf) # remove the leaf node
                if len (neighbors[n1]) == 1:
                    new_leaves.append (n1)
            leaves = new_leaves
        return leaves
