# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        new = None
        current = head
        while current:
            newN = current.next
            current.next = new
            new = current
            current = newN

        while new and head:
            if new.val != head.val : 
                return False
            new = new.next
            head = head.next
        return True
        
