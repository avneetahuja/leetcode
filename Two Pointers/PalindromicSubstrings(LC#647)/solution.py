class Solution:
    def countSubstrings(self, s: str) -> int:
        #at each index treat that as middle to find odd length palindromes and 
        #i and i+1 as middle to find even length palindromes
        c=0
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                c+=1
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                c+=1
                l-=1
                r+=1
        return c
