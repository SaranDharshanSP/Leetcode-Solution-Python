# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count = 0
        dummy = ListNode(0)
        dummy.next = list1
        current = list1

        while count < a-1:
            count+=1
            current = current.next
        ha = current

        while count < b+1:
            count+=1
            current = current.next
        hb = current

        ha.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = hb

        return dummy.next
            