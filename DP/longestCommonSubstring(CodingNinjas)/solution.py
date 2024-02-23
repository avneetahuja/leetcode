def lcs(x: str, y: str) -> int:
    # write your code here
    m,n = len(x),len(y)
    maxx=0
    t = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:

                t[i][j] = 1+t[i-1][j-1]
                maxx=max(t[i][j],maxx)
            else:
                t[i][j] = 0
    return maxx
