class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1
 
        s=s.lower()
        print(s)
        while p1<p2:
            while(p1<p2 and not s[p1].isalnum()):
                p1+=1
            while(p1<p2 and not s[p2].isalnum()):
                p2-=1
            if s[p1]!=s[p2]:
                print(s[p1],s[p2])
                return False
            p1+=1
            p2-=1
        return True
