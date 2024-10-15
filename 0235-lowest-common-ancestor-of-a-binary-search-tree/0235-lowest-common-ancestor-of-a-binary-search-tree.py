# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if q.val > curr.val and p.val > curr.val:
                curr = curr.right
            elif q.val < curr.val and p.val < curr.val:
                curr = curr.left
            else:
                return curr