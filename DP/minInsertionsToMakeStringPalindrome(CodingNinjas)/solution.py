from sys import *
from collections import *
from math import *

def minInsertion(str):
    # Write the function here.
    m=len(str)
    s = str[::-1]
    t = [[0 for i in range(m+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,m+1):
            if str[i-1] == s[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])

    return m - t[m][m]
