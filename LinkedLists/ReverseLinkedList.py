# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
        
        prev = None
        curr = head
        
        while curr: # looping condition
            nxt = curr.next # none
            curr.next = prev # swap 5 - 4 -  3 - 2 - 1 - none
            prev = curr # 5
            curr = nxt # none
        return prev
