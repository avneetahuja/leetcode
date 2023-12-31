class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j,mostFreq,lCount,ans = 0,0,0,{},0
        while j< len(s):
            lCount[s[j]] = 1 + lCount.get(s[j],0)
            mostFreq = max(mostFreq,lCount[s[j]])

            while j-i+1-mostFreq>k:
                lCount[s[i]]-=1
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans
