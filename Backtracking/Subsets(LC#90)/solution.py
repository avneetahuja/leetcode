class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def f(i,li):
            if li not in res:
                res.append(li)
            for ind in range(i,len(nums)):
                f(ind+1,li+[nums[ind]])
                while(ind<len(nums)-1 and nums[ind+1]==nums[ind]):
                    ind+=1
        f(0,[])
        return res
