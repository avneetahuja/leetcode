class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = len(prices)
        t = [[0 for i in range(2)] for j in range(p+1)]
        for i in range(p-1,-1,-1):
            for j in range(2):
                if j == 1:
                    t[i][j] = max(-prices[i] + t[i+1][0], t[i+1][1])
                else:
                    if i==p-1:
                        t[i][j] = max(prices[i],t[i+1][0])
                    else:
                        t[i][j] = max(prices[i]+t[i+2][1],t[i+1][0])
        return t[0][1]
