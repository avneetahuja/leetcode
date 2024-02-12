# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            self.res.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return self.res[k-1]
