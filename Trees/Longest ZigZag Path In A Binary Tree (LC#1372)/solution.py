# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_path_length = 0
        def dfs(node,need_left,current_length):
            nonlocal max_path_length
            if not node:
                return
            max_path_length = max(current_length,max_path_length)
            if need_left:
                dfs(node.left,False,current_length+1)
                dfs(node.right,True,1)
            else:
                dfs(node.right,True,current_length+1)
                dfs(node.left,False,1)
        dfs(root,False,0)
        dfs(root,True,0)
        return max_path_length
        
