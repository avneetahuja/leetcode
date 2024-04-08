from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            n = len(q)
            curlevel = []
            for i in range(n):
                node = q.popleft()
                q.extend(node.children)
                curlevel.append(node.val)
            res.append(curlevel)
        return res
