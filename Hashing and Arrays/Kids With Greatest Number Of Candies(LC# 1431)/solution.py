class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        mx = max(candies)
        for i in range(len(res)):
            if candies[i]+extraCandies>=mx:
                res[i]=True
        return res
