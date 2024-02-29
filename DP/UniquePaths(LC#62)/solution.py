class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [[-1 for i in range(n)] for j in range(m)]
        def f(i,j):
            if i==m-1:
                return 1
            if j==n-1:
                return 1
            if t[i][j]!=-1:
                return t[i][j]
            t[i][j] = f(i+1,j) + f(i,j+1)
            return t[i][j]
        return f(0,0)
