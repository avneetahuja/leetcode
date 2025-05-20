class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        q = deque([(root, 0)])
        while q:
            node, lvl = q.popleft()
            if lvl == len(ans):
                ans.append([node.val])
            else:
                ans[lvl].append(node.val)
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
        for i in range(1, len(ans), 2):
            ans[i].reverse()
        return ans
