class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lCount={}
        for c in s1:
            lCount[c] = 1 + lCount.get(c,0)
        print(lCount)
        k,count,i,j = len(s1),len(lCount),0,0
        while j<len(s2):
            if s2[j] in lCount:
                lCount[s2[j]]-=1
                if lCount[s2[j]]==0:
                    count-=1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if count==0:
                    return True
                if s2[i] in lCount:
                    lCount[s2[i]]+=1
                    if lCount[s2[i]]==1:
                        count+=1
                i+=1
                j+=1
        return False
