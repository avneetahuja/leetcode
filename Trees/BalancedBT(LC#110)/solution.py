class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightAndBalanced(node):
            if not node:
                return [0,True]
            l,r = heightAndBalanced(node.left),heightAndBalanced(node.right)
            isBalanced = (l[1] and r[1] and abs(l[0]-r[0])<=1)
            return [1+max(l[0],r[0]),isBalanced]
        return heightAndBalanced(root)[1]
