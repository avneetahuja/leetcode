class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def f(i,li):
            if i==len(s):
                res.append(li)
                return
            for ind in (i,len(s)):
                sub = s[i:ind+1]
                if sub!= '' and sub == sub[::-1]:
                    f(ind+1,li+[sub])
        f(0,[])
        return res
