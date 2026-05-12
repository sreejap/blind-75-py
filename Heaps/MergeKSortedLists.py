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
