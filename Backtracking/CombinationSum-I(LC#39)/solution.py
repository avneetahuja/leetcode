class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        def f(i,s,li):
            if i==len(candidates):
                return
            if s<0:
                return
            if s==0:
                res.append(li)
                return
            f(i,s-candidates[i],li+[candidates[i]])
            f(i+1,s,li)
        f(0,target,[])
        return res
