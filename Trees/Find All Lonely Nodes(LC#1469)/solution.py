# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def search(node):
            if not node:
                return
            if node.left and node.right:
                search(node.left)
                search(node.right)
            elif node.left:
                res.append(node.left.val)
                search(node.left)
            elif node.right:
                res.append(node.right.val)
                search(node.right)
        search(root)
        return res
