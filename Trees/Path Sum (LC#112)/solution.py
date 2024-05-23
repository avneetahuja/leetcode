# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(node,running_sum):
            if not node:
                return False
            if not node.left and not node.right:
                return node.val + running_sum == targetSum
            return search(node.left,node.val+running_sum) or search(node.right,node.val+running_sum)
        return search(root,0)
