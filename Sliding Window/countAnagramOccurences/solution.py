class Solution:
    def countSubstringAnagrams(self,str,sub):
        lcount = {}
        for c in sub:
            lcount[c] = 1 + lcount.get(c,0)
        count = len(lcount)#distinct letter count
        k = len(sub)#window size
        i,j=0,0
        anagramCount = 0 
        while(j<len(str)):
            if str[j] in lcount:
                lcount[str[j]]-=1
                if lcount[str[j]] == 0:
                    count-=1
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                if count==0:
                    # print(i,j)
                    anagramCount+=1
                j+=1
                if str[i] in lcount:
                    lcount[str[i]]+=1
                    if lcount[str[i]]==1:
                        count+=1
                i+=1
        return anagramCount
