    def minNumberOfOpsToMakeTwoStringsEqual(self, x: str, y: str) -> int:
        m,n = len(x),len(y)
        t = [[0 for i in range(n+1)]for j in range(m+1)]
        # res = "" If you want to print it
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1] == y[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                    # res +=x[i-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        # print(res)
        return m+n-2*t[m][n]
