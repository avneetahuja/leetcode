def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        answer = []

        def search(node, current_path):
            if not node:
                return
            if node == p:
                answer.append(current_path + [node])
            if node == q:
                answer.append(current_path + [node])
            search(node.left, current_path + [node])
            search(node.right, current_path + [node])

        search(root, [])
        
        if len(answer) != 2:
            return None
        
        path_p = answer[0]
        path_q = answer[1]

        lca = None
        for u, v in zip(path_p, path_q):
            if u == v:
                lca = u
            else:
                break

        return lca
