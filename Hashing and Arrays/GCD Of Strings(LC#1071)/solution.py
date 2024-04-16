class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        n = len(str1)
        m = len(str2)
        for i in range(min(n,m)):
            if str1[:i+1]==str2[:i+1] and ((n/(i+1))%1==0) and ((m/(i+1))%1==0):
                res=str1[:i+1]

        r = len(res)
        if r==0:
            return ""
        c1 = n//r
        c2 = m//r
        for j in range(1,c1):
            if str1[r*j:r*(j+1)] != res:
                return ""
        for j in range(1,c2):
            if str2[r*j:r*(j+1)] != res:
                return ""
        return res
