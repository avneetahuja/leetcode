class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        v = [1] * n
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    v[i] = max(v[i],1 + v[j])
        return max(v)
