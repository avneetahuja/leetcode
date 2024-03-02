class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = [0] * len(prices)
        # def f(i,s):
        #     if i<0:
        #         return
        #     if s==0:
        #         f(i-1,prices[i])
        #         f(i-1,0)
        #     if profits[i] > s-prices[i]:
        #         return
        #     if prices[i]>=s:
        #         f(i-1,s)
        #     else:
        #         profits[i] = s-prices[i]
        #         f(i-1,0)
        # f(len(prices)-1,0)
        # # print(profits)
        # return sum(profits)
        n = len(prices)
        t = [[-1 for i in range(2)] for j in range(n)]
        def f(i,canBuy):
            if i==n:
                return 0
            if t[i][canBuy]!=-1:
                return t[i][canBuy]
            if canBuy==1:
                t[i][canBuy] = max(-prices[i]+f(i+1,0), f(i+1,1))
            else:
                t[i][canBuy] = max(prices[i]+f(i+1,1),f(i+1,0))
            return t[i][canBuy]
        return f(0,1)
