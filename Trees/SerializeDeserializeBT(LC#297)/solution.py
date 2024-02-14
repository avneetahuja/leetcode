# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = ""
        def preOrder(node):
            nonlocal res
            if not node:
                res+="N,"
                return
            res += str(node.val)+","
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return res[:len(res)-1]

        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(",")
        index = 0
        def build():
            nonlocal index
            if nodes[index]=="N":
                index+=1
                return
            node = TreeNode(int(nodes[index]))
            index+=1
            node.left = build()
            node.right = build()
            return node
        return build()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
