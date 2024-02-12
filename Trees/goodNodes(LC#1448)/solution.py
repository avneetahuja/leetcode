# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.goodCount = 0
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def count(node,val):
            if not node:
                return
            if val<=node.val:
                val = node.val
                self.goodCount+=1
            count(node.left,val)
            count(node.right,val)
        count(root,root.val)
        return self.goodCount
