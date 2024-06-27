# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new = TreeNode(-1)
        tail = new
        def ino(node):
            if not node:
                return 
            ino(node.left)
            nonlocal tail
            tail.right = node
            tail.left =None
            tail = tail.right
            tail.left = None
            ino(node.right)
            tail.right= None
        ino(root)
        return new.right
