"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        def clone(node):
            if not node:
                return node
            if node in visited:
                return visited[node]
            newNode = Node(node.val)
            visited[node] = newNode
            for neighbour in node.neighbors:
                newNode.neighbors.append(clone(neighbour))
            return newNode

        return clone(node)
