class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,mx,lcount=0,0,0,{}
        while j<len(s):
            lcount[s[j]]=1+lcount.get(s[j],0)
            if len(lcount)==j-i+1:
                mx = max(mx,j-i+1)
                j+=1
            elif len(lcount)<j-i+1:
                while len(lcount)<j-i+1:
                    lcount[s[i]]-=1
                    if lcount[s[i]]==0:
                        del lcount[s[i]]
                    i+=1
                j+=1
        return mx
