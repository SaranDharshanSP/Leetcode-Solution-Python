# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return head
        new = None
        current = head 
        while current :
            nextN = current.next
            current.next = new
            new = current
            current = nextN
        return new