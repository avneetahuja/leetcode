class Solution:
    def numDistinct(self, x: str, y: str) -> int:
        t = [[-1 for i in range(len(x))] for j in range(len(y))]
        def f(m,n):  
            if m<0:
                return 1
            if n<0:
                return 0
            if t[m][n]!=-1:
                return t[m][n]
            if x[n]==y[m]:
                t[m][n] = f(m,n-1)+f(m-1,n-1)
            else:
                t[m][n] = f(m,n-1)
            return t[m][n]
        return f(len(y)-1,len(x)-1)
