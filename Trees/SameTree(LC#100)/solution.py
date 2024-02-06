# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
 
        def compare(p,q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if q and not p:
                return False
            if not p.val == q.val:
                return False
            l = compare(p.left,q.left)
            r = compare(p.right,q.right)
            return l and r
        return compare(p,q)
