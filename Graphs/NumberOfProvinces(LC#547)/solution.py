class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {}
        adjList = {}
        def search(i,flag):
            if i in visited:
                return
            visited[i] = True
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    search(j,False)
                    if flag:
                        if i in adjList:
                            adjList[i].append(j)
                        else:
                            adjList[i] = [j]  
            return
        
        for i in range(len(isConnected)):
            search(i,True)
        return len(adjList)
