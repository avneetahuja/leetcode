class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(piles,k):
            total=0
            for pile in piles:
                total+=math.ceil(pile/k)
            return total
        l,r=1,max(piles)
        while l<=r:
            m=l+(r-l)//2
            if getHours(piles,m)<=h:
                r=m-1
            else:
                l=m+1
        return l
