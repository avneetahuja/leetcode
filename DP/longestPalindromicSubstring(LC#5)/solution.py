class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = s[::-1]
        m = len(s)
        maxx = 0
        end=0
        start =-1
        t = [[0 for i in range(m+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,m+1):
                if s[i-1]==r[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                    sub = s[i-t[i][j]:i]
                    if t[i][j]>maxx and (sub==sub[::-1]):
                        maxx = t[i][j]
                        end = i
                        start = end - t[i][j]
                else:
                    t[i][j]=0
        return s[start:end]
