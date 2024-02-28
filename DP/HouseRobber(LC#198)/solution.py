class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        v = [0]*(n+1)
        v[1] = nums[0]
        for i in range(2,n+1):
            v[i] = max(nums[i-1]+v[i-2],v[i-1])
        return v[n]
