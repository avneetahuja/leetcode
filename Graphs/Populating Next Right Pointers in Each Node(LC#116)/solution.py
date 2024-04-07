from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                cur = q.popleft()
                if i<l-1:
                    cur.next = q[0]
                if cur.left:
                    q.append(cur.left)
                    q.append(cur.right)
        return root
