class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def f(i,li):
            if len(li)==len(nums):
                res.append(li)
            for ind in range(0,len(nums)):
                if nums[ind] in li:
                    continue
                else:
                    f(ind+1,li+[nums[ind]])
        f(0,[])
        return res
