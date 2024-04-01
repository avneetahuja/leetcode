class Solution:
    def shortestCommonSupersequence(self, x: str, y: str) -> str:
        m,n = len(x),len(y)
        t = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1]==y[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        i,j = m,n
        ans = ""
        while i>0 and j>0:
            if i>0 and j>0 and x[i-1]==y[j-1]:
                ans = x[i-1] + ans
                i-=1
                j-=1
            elif t[i-1][j]>t[i][j-1]:
                ans = x[i-1]+ans
                i-=1
            else:
                ans = y[j-1]+ans
                j-=1
        while i>0:
            ans = x[i-1]+ans
            i-=1
        while j>0:
            ans = y[j-1]+ans
            j-=1
        return ans
