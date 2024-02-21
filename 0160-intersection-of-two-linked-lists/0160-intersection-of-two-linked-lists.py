# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left = headA
        right = headB
        while left != right:
            left = headB if left is None else left.next
            right = headA if right is None else right.next
        return left
