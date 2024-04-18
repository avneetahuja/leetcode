class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)<=1:
            return len(chars)

        s = ""
        n = len(chars)
        i=0
        while i<=n-1:
            cur = 1
            while i<n-1 and chars[i]==chars[i+1]:
                cur+=1
                i+=1
            s+=chars[i]
            i+=1
            if cur>1:    
                s+=str(cur)
        for j in range(len(s)):
            chars[j] = s[j]
        return len(s)
