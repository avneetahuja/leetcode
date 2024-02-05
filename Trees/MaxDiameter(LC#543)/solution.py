# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxD=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam(node):
            if not node:
                return 0
            lh = diam(node.left)
            rh = diam(node.right)
            self.maxD = max(self.maxD,lh+rh)
            return 1+max(lh,rh)
        diam(root)
        return self.maxD
