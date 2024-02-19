class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        s = sum(stones)
        t=[]
        n = len(stones)
        t = [[False for j in range(s+1)] for i in range(n+1)]
        for i in range(n+1):
            t[i][0] = True
        for i in range(1,n+1):
            for j in range(1,s+1):
                if stones[i-1]<=j:
                    t[i][j] = t[i-1][j-stones[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        for i in range(s//2,0,-1):
            if t[n][i]:
                return s-2*i
        return stones[0]
