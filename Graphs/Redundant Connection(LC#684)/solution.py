class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        def find(i):
            if i == root[i]:
                return i
            root[i] = find(root[i])
            return root[i]
        def union(i,j):
            ri = find(i)
            rj = find(j)
            if ri != rj:
                if rank[ri]>rank[rj]:
                    root[rj] = ri
                elif rank[rj]>rank[ri]:
                    root[ri] = rj
                else:
                    root[rj] = ri
                    rank[ri]+1
            
        for start,end in edges:
            start-=1
            end-=1
            if find(start)==find(end):
                return [start+1,end+1]
            union(start,end)
