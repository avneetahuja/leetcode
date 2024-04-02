class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs, key=lambda x: x[0])
        rank = [1] * n
        root = [i for i in range(n)]
        c = n
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
                if rank[rI]>rank[rJ]:
                    root[rJ] = rI
                elif rank[rJ]>rank[rI]:
                    root[rI] = rJ
                else:
                    root[rJ] = rI
                    rank[rI]+=1
                c-=1
        for log in logs:
            union(log[1],log[2])
            if c==1:
                return log[0]
        return -1
