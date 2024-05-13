class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        l,r,count,max_count = 0,0,0,0
        n = len(s)
        while r<n:
            if r-l+1<k:
                if s[r] in vowels:
                    count+=1
                r+=1
            else:
                if s[r]in vowels:
                    count+=1
                max_count = max(max_count,count)
                r+=1
                if s[l] in vowels:
                    count-=1
                l+=1
        return max_count
