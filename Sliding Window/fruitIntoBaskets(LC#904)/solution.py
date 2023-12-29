class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i,j,mx,fCount = 0,0,0,{}
        while j<len(fruits):
            fCount[fruits[j]] = 1 + fCount.get(fruits[j],0)
            if len(fCount)<=2:
                mx = max(mx,j-i+1)
                j+=1
            else:
                while len(fCount)>2:
                    fCount[fruits[i]]-=1
                    if fCount[fruits[i]]==0:
                        del fCount[fruits[i]]
                    i+=1
                j+=1
        return mx
