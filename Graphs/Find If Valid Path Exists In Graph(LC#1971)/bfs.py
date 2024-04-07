from collections import deque 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for s,e in edges:
            adjList[s].append(e)
            adjList[e].append(s)
        q = deque()
        q.append(source)   
        seen = {source:True}
        while q:
            cur = q.popleft()
            if cur==destination:
                return True
            for node in adjList[cur]:
                if not node in seen:
                    q.append(node)
                    seen[node] = True
        return False
