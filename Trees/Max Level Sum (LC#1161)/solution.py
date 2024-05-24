import numpy as np
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sums =[]
        def search(node,level):
            if not node:
                return
            if level>len(level_sums):
                level_sums.append(node.val)
            else:
                level_sums[level-1]+=node.val
            search(node.left,level+1)
            search(node.right,level+1)
        search(root,1)
        level_sums = np.array(level_sums)

        return np.argmax(level_sums)+1
        
