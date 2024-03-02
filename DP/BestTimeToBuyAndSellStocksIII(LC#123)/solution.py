class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t = [[[-1 for i in range(3)]for j in range(2)]for k in range(len(prices))]
        def f(i,b,c):
            if i==len(prices) or c==2:
                return 0
            if t[i][b][c]!=-1:
                return t[i][b][c]
            if b==1:
                t[i][b][c] = max(-prices[i]+f(i+1,0,c),f(i+1,1,c))
            else:
                t[i][b][c] = max(prices[i]+f(i+1,1,c+1),f(i+1,0,c))
            return t[i][b][c]
        return f(0,1,0)
        
