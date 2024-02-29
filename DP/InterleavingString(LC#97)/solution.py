class Solution:
    def isInterleave(self, x: str, y: str, z: str) -> bool:
        t = [[-1 for i in range(len(y))] for j in range(len(x))]
        def f(m,n,r):
            if m<0:
                return y[:n+1]==z[:r+1]
            if n<0:
                return x[:m+1]==z[:r+1]
            if r<0 or (x[m]!=z[r] and y[n]!=z[r]):
                return False
            if t[m][n]!=-1:
                return t[m][n]
            if x[m]==z[r] and y[n]==z[r]:
                t[m][n] = f(m-1,n,r-1) or f(m,n-1,r-1)
            elif x[m]==z[r]:
                t[m][n] = f(m-1,n,r-1)
            else:
                t[m][n] =  f(m,n-1,r-1)
            return t[m][n]
        return f(len(x)-1,len(y)-1, len(z)-1)
