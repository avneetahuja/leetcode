class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        i =0
        map={}
        res = []
        while i<=len(s)-10:
            j=i+10
            map[s[i:j]] = 1+ map.get(s[i:j],0)
            if map[s[i:j]]==2:
                res.append(s[i:j])
            i+=1
        return res
