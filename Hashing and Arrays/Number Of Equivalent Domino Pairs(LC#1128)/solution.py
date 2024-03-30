import math
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = {}
        count = 0
        for d in dominoes:
            d.sort()
            if (d[0],d[1]) in seen:
                seen[(d[0],d[1])] += 1
            else:
                seen[(d[0],d[1])] = 1
        for key,value in seen.items():
            if value>1:
                count+=math.comb(value,2)
        return count
