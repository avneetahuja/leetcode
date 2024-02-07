# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = ""
        self.res2 = ""
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preOrderRoot(node):
            if not node:
                self.res+="null"
                return
            if node.val>10:
                self.res+=str(node.val)+"."
            else:
                self.res+=str(node.val)
            preOrderRoot(node.left)
            preOrderRoot(node.right)
        def preOrderSubRoot(node):
            if not node:
                self.res2+="null"
                return
            if node.val>10:
                self.res2+=str(node.val)+"."
            else:
                self.res2+=str(node.val)
            preOrderSubRoot(node.left)
            preOrderSubRoot(node.right)
        
        preOrderRoot(root)
        preOrderSubRoot(subRoot)
        return self.res2 in self.res
