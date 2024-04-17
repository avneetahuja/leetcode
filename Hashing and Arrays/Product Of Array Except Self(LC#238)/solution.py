class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0] * n
        l[0] = 1
        for i in range(1,n):
            l[i] = nums[i-1]*l[i-1]
        r = nums[n-1]
        for i in range(n-2,-1,-1):
            l[i] *= r
            r *= nums[i]
        return l
