# https://leetcode.com/problems/merge-k-sorted-lists/
# Time complexity : O(Nlogk) where k is the number of linked lists.

# The comparison cost will be reduced to O(logk) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.
# There are N nodes in the final linked list.
# Space complexity :

# O(n) Creating a new linked list costs O(n) space.
# O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).

from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class HeapNode:
    def __init__(self,node):
        self.node = node
    
    def __lt__(self,other):
        return self.node.val < other.node.val
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode (0)
        curr = dummy
        heap = []

        for l in lists:
            if l:
                heapq.heappush (heap,HeapNode(l))
        
        while heap:
            heap_node = heapq.heappop(heap)
            curr.next = heap_node.node
            curr = curr.next
            if heap_node.node.next:
                heapq.heappush (heap, HeapNode(heap_node.node.next))

        return dummy.next
