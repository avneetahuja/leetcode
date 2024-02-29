class Solution:
    def minDistance(self, x: str, y: str) -> int:
        t = [[-1 for i in range(len(y))]for j in range(len(x))]
        def f(m,n):
            if m<0:
                return n+1
            if n<0:
                return m+1
            if t[m][n] != -1:
                return t[m][n]
            if x[m]==y[n]:
                t[m][n] = f(m-1,n-1)
            else:
                t[m][n] = 1 + min(f(m-1,n),f(m-1,n-1),f(m,n-1))
            return t[m][n]
        return f(len(x)-1,len(y)-1)
