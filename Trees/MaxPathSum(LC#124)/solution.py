# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val
        def findMaxSum(node):
            if not node:
                return 0
            l = findMaxSum(node.left)
            r = findMaxSum(node.right)
            l = max(l,0)
            r = max(r,0)
            self.res = max(self.res,l+r+node.val)
            return node.val+max(l,r)
        findMaxSum(root)
        return self.res
