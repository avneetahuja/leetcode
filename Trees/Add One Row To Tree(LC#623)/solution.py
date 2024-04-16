from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            newNode = TreeNode(val,root,None)
            return newNode
        q= deque()
        q.append((root,1))
        while q:
            curNode,curLevel = q.popleft()
            if curLevel == depth-1:
                newNode = TreeNode(val,curNode.left,None)
                curNode.left = newNode
                newNode = TreeNode(val,None,curNode.right)
                curNode.right = newNode
                continue
            if curNode.left:
                q.append((curNode.left,curLevel+1))
            if curNode.right:
                q.append((curNode.right,curLevel+1))
        return root
