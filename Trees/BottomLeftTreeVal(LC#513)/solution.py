# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.left=10000
        self.lastLevel = -1
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def find(node,level):
            if not node:
                return
            if level>self.lastLevel:
                self.lastLevel = level
                self.left = node.val
            find(node.left,level+1)
            find(node.right,level+1)
        find(root,0)
        return self.left
        
