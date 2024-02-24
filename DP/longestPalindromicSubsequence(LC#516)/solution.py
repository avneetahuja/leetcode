class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        m = len(s)
        t = [[0 for i in range(m+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,m+1):
                if s[i-1]==s2[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        return t[m][m]
