# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest = "zzzzzzzzzzzzzzzzzzzzzzzz"
        cur = ""
        def dfs(node,cur):
            nonlocal smallest
            cur = chr(node.val+ord('a')) + cur
            l,r = node.left,node.right
            if not l and not r and cur<smallest:
                smallest = cur    
            if l:
                dfs(l,cur)
            if r:
                dfs(r,cur)
        dfs(root,"")
        return smallest
