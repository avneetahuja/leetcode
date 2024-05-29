class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        count=0
        for start,end in connections:
            adjList[start].append([end,1])
            adjList[end].append([start,0])
        stack =[0]
        visited ={}
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            else:
                visited[node] = True
                for n,sign in adjList[node]:
                    if not n in visited:
                        if sign==1:
                            count+=1
                        stack.append(n)
        return count
