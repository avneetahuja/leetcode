class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = {}
        edgeCount = len(edges)
        for start,end in edges:
            if start in graph:
                graph[start].append(end)
            else:
                graph[start] = [end]
        if destination in graph:
            return False
        t = {}
        def dfs(node,c):
            if node not in graph:
                return node==destination
            if node in t:
                return True
            if c > edgeCount:
                return False
            for neighbor in graph[node]:
                if not dfs(neighbor,c+1):
                    return False
                else:
                    t[neighbor] = True
            return True
        return dfs(source,0)
        
