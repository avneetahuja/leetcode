class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        root = [i for i in range(n)]
        rank = [1] * n
        c=n
        def find(i):
            if root[i]==i:
                return i
            root[i] = find(root[i])
            return root[i]
        def union(i,j):
            nonlocal c
            rI = find(i)
            rJ = find(j)
            if rI!=rJ:
                if rank[rI] > rank[rJ]:
                    root[rJ] = rI
                elif rank[rJ]>rank[rI]:
                    root[rI] = rJ
                else:
                    root[rJ] = rI
                    rank[rI]+=1
                c-=1
        for edge in edges:
            union(edge[0],edge[1])
        return c==1
