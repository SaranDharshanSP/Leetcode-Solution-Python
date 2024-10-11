# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = set()
        while head:
            if head.next not in a:
                a.add(head.next)
            else: return True
            head = head.next
        return False