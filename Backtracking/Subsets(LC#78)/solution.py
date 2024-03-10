class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[]
        def f(i,li):
            res.append(li)
            for ind in range(i,len(nums)):
                f(ind+1,li+[nums[ind]])
        f(0,[])
        return res
