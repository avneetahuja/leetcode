class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1=0
        res=""
        limit = min(len(word1),len(word2))
        while p1<limit:
            res+=word1[p1]
            res+=word2[p1]
            p1+=1
        if len(word1)>len(word2):
            return res+word1[p1:]
        elif len(word2)>len(word1):
            return res+word2[p1:]
        return res
