class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)
        l,r=0,len(s)-1
        while l<r:
            if s[l] in vowels:
                while s[r] not in vowels:
                    r-=1
                temp=s[l]
                s[l] = s[r]
                s[r]=temp
            elif s[r] in vowels:
                while s[l] not in vowels:
                    l+=1
                temp=s[l]
                s[l] = s[r]
                s[r]=temp       
            l+=1
            r-=1
        return "".join(s)
