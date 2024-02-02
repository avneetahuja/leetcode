# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q,res=[],[]
        if root:
            q.append(root)
        while q:
            
            vals=[]
            for i in range(len(q)):
                node = q[0]
                q = q[1:] if len(q)>=1 else []
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(vals)
        return res
