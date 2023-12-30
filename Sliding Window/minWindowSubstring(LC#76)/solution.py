class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        lcount = {}
        for c in t:
            lcount[c] = 1+lcount.get(c,0)
        print(lcount)
        count = len(lcount)
        mn=""
        i,j=0,0
        while j<len(s):
            if s[j] in lcount:
                lcount[s[j]]-=1
                if lcount[s[j]]==0:
                    count-=1
            if count==0:
                if len(s[i:j+1])<len(mn) or mn=="":
                    mn = s[i:j+1]
                while(count==0):
                    if s[i] in lcount:
                        lcount[s[i]]+=1
                        if lcount[s[i]]==1:
                            count+=1
                            if len(s[i:j+1])<len(mn) or mn=="":
                                mn = s[i:j+1]
                    i+=1
            j+=1


        return mn
