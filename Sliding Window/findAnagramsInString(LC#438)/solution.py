class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        lcount = {}
        for c in p:
            lcount[c] = 1 + lcount.get(c,0)
        count = len(lcount)
        i,j,aCount = 0,0,[]
        while j<len(s):
            if s[j] in lcount:
                lcount[s[j]]-=1
                if lcount[s[j]]==0:
                    count-=1
            
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if count==0:
                    aCount.append(i)
                j+=1
                if s[i] in lcount:
                    lcount[s[i]]+=1
                    if lcount[s[i]]==1:
                        count+=1
                i+=1
        return aCount
