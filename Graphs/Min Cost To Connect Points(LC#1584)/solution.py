class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        total = 0
        edgeCount =0

        root = [i for i in range(n)]
        rank = [1]*n
        def find(i):
            if i==root[i]:
                return i
            root[i] = find(root[i])
            return root[i]
        
        def union(i,j):
            ri = find(i)
            rj = find(j)
            if ri!=rj:
                if rank[i]>rank[j]:
                    root[rj]=ri
                elif rank[i]<rank[j]:
                    root[ri] = rj
                else:
                    root[rj] = ri
                    rank[ri]+=1
        
        def connected(i,j):
            return find(i)==find(j)

        for i in range(n):
            for j in range(i+1,n):
                cost = abs(points[j][1]-points[i][1]) + abs(points[j][0]-points[i][0])
                edges.append([cost,i,j])
        edges.sort()
        for edge in edges:
            if connected(edge[1],edge[2]):
                continue
            union(edge[1],edge[2])
            total+=edge[0]
            edgeCount+=1
            if edgeCount==n-1:
                break
        return total
