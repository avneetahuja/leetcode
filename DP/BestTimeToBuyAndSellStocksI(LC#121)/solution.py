class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx=0
        minSoFar = prices[0]
        for i in range(1,len(prices)):
            minSoFar = min(prices[i],minSoFar)
            maxx = max(prices[i]-minSoFar,maxx)
        return maxx
