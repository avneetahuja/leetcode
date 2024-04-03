class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        root = [i for i in range(n)]
        rank = [1] * n
        def find(i):
            if root[i]==i:
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
                    rank[ri] += 1
        def connected(i,j):
            return find(i)==find(j)
        for edge in edges:
            union(edge[0],edge[1])
        return connected(source,destination)
