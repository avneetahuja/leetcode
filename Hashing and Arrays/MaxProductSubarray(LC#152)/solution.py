class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # THIS AINT DP, This based on prefix and suffix products
        pre,suf,maxx = 1,1,-10**9
        for i in range(len(nums)):
            if pre==0:
                pre=1
            if suf==0:
                suf=1
            pre*=nums[i]
            suf*=nums[len(nums)-1-i]
            maxx = max(pre,suf,maxx)
        return maxx
