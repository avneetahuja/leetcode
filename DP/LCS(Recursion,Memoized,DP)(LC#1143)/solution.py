class Solution:
    
    ##Recursive Solution
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     return self.recFunc(text1,text2)

    # def recFunc(self,text1,text2):
    #     if len(text1)==0 or len(text2)==0:
    #         return 0
    #     if text1[-1] == text2[-1]:
    #         return 1 + self.recFunc(text1[:-1],text2[:-1])
    #     else:
    #         return max(self.recFunc(text1,text2[:-1]),self.recFunc(text1[:-1],text2))


    ## Memoized Version
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     m,n = len(text1),len(text2)
    #     t = [[-1 for i in range(n+1)]for j in range(m+1)]
    #     def memFunc(x,y,m,n):
    #         nonlocal t
    #         # print(m,n)
    #         if t[m][n] != -1:
    #             return t[m][n]
            
    #         if m==0 or n==0:
    #             t[m][n] = 0
    #         elif x[m-1]==y[n-1]:
    #             t[m][n] = 1 + memFunc(x,y,m-1,n-1)
    #         else:
    #             t[m][n] = max(memFunc(x,y,m-1,n),memFunc(x,y,m,n-1))
    #         return t[m][n]
    #     memFunc(text1,text2,m,n)
    #     return t[m][n]

    ## Bottom UP DP
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        m,n = len(x),len(y)
        t = [[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if x[i-1] == y[j-1]:
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])
        return t[m][n]
        

    
