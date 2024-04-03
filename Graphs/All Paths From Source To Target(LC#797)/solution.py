class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        def search(node,li):
            if node == target:
                li.append(target)
                res.append(li)
            for neighbour in graph[node]:
                search(neighbour,li+[node])
        search(0,[])
        return res
