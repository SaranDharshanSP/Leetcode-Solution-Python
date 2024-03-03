# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        count = 0
        while current.next:
            current = current.next
            count+=1
        current = dummy
        for i in range(count-n):
                current = current.next

        current.next = current.next.next
        return dummy.next

