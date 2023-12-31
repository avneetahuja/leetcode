class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j,maxD,minSoFar=0,0,0,float('inf')
        while j< len(prices):
            if prices[j]<minSoFar:
                minSoFar = prices[j]
                i=j
            maxD = max(maxD,prices[j]-prices[i])
            j+=1
        return maxD
