# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rightSide = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def addToRight(node,level):
            if not node:
                return
            if level == len(self.rightSide):
                self.rightSide.append(node.val)
            addToRight(node.right,level+1)
            addToRight(node.left,level+1)
        addToRight(root,0)
        return self.rightSide
