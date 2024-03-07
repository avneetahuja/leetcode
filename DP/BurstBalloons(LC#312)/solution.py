class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## We are going to start from behind rather than front, this is a very
        ## hard problem to solve on my own, watch striver's vid again if needed
        ## so imagine you just have one ballon at the end and you trace your way back...
        n=len(nums)
        # t = [[-1 for i in range(n)]for j in range(n)]#for memoisation
        def f(i,j):
            if i>j:
                return 0
            if t[i][j]!=-1:
                return t[i][j]
            maxi = -inf
            for ind in range(i,j+1):
                left = 1 if i==0 else nums[i-1]
                right = 1 if j==n-1 else nums[j+1]
                cost = left*nums[ind]*right + f(i,ind-1) + f(ind+1,j)
                maxi=max(maxi,cost)
            t[i][j] = maxi
            return t[i][j]


        #Tabulation    
        t = [[0 for i in range(n+1)]for j in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(n):
                if i>j:
                    continue
                maxi = -inf
                for ind in range(i,j+1):
                    print
                    left = 1 if i==0 else nums[i-1]
                    right = 1 if j>=n-1 else nums[j+1]
                    cost = left*nums[ind]*right + f(i,ind-1) + f(ind+1,j)
                    maxi=max(maxi,cost)
                t[i][j] = maxi
        return t[0][n-1]
