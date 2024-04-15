# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        def dfs(node, s):
            nonlocal total
            l = node.left
            r = node.right
            if not l and not r:
                s+=str(node.val)
                total += int(s)
            if l:
                dfs(l,s+str(node.val))
            if r:
                dfs(r,s+str(node.val))
        dfs(root,"")
        return total
