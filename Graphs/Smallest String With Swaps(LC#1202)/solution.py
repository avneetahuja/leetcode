class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root = [i for i in range(n)]
        rank = [1] * n
        def find(i):
            if i==root[i]:
                return i
            root[i] = find(root[i])
            return root[i]
        def union(i,j):
            ri = find(i)
            rj = find(j)
            if ri!=rj:
                if rank[ri]>rank[rj]:
                    root[rj] = ri
                elif rank[rj]>rank[ri]:
                    root[ri] = rj
                else:
                    root[rj] = ri
                    rank[ri]+=1
        for pair in pairs:
            union(pair[0],pair[1])
        roots = {}
        res = " "
        s = list(s)
        for i in range(n):
            r = find(i)
            if r in roots:
                roots[r].append(i)
            else:
                roots[r]=[i]
        for v in roots.values():
            st=[]
            for c in v:
                st.append(s[c])
            st.sort()
            i=0
            for c in v:
                s[c] = st[i]
                i+=1
        return ''.join(s)
