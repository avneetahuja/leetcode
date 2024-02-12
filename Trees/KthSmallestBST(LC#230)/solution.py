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
            
            if len(self.res)==k:
                return
            self.res.append(node.val)
            inOrder(node.right)
        inOrder(root)
        # print(self.res)
        return self.res[-1]
        
        
