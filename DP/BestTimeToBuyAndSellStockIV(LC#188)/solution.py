class Solution:
    def maxProfit(self, c: int, prices: List[int]) -> int:
        p=len(prices)
        after = [[0 for _ in range(c+1)] for _ in range(2)]
        cur = [[0 for _ in range(c+1)] for _ in range(2)]
        for i in range(p-1,-1,-1):
            for j in range(2):
                for k in range(c-1,-1,-1):
                    if j==1:
                        cur[j][k] = max(-prices[i]+after[0][k],after[1][k])
                    else:
                        cur[j][k] = max(prices[i]+after[1][k+1],after[0][k])
            after = cur
        return cur[1][0]
