class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i,n in enumerate(nums):
            comp = target - n
            if comp in comps:
                return [i,comps[comp]]
            else:
                comps[n] = i
