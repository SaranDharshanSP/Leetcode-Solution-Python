import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            gcd_value = math.gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd_value)
            gcd_node.next = current.next
            current.next = gcd_node
            current = gcd_node.next

        return head
