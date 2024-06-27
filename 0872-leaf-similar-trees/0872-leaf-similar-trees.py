# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righndt
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def find(node: Optional[TreeNode]):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return find(node.left)+ find(node.right)
        l = find(root1)
        r = find(root2)

        return l==r


        