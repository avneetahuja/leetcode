from os import *
from sys import *
from collections import *
from math import *

def longestRepeatingSubsequence(st, n):

    m = len(st)
    t = [[0 for i in range(m+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,m+1):
            if st[i-1] == st[j-1] and i != j:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[m][m]
