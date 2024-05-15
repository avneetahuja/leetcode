class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0
        def traversal(node):
            nonlocal range_sum
            if not node:
                return
            if low<=node.val<=high:
                range_sum+=node.val
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        return range_sum
