class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if sorted(s)!=sorted(goal):
            return False
        res = ""
        seen ={}
        maxC = 0
        for i in range(len(s)):
            if s[i]!=goal[i]:
                res+=s[i]
            seen[s[i]] = 1+ seen.get(s[i],0)
            maxC = max(maxC,seen[s[i]])
        if len(res)==2:
            return True
        if maxC>1 and len(res)<3:
            return True
