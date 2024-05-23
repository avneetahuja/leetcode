# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans =[]
        def search(node,current_path):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                if node.val+sum(current_path)==targetSum:
                    current_path.append(node.val)
                    ans.append(current_path)
                    return
            search(node.left,current_path+[node.val])
            search(node.right,current_path+[node.val])
        search(root,[])
        return ans
