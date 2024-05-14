class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums)-1
        k=1
        l,r,max_length,current_count = 0,0,0,0
        while r < len(nums):
            if nums[r]==0:
                current_count+=1
            if current_count<=k:
                max_length = max(max_length,r-l+1)
                r+=1
            else:
                while l<len(nums) and nums[l]!=0:
                    l+=1
                l+=1
                r+=1
                current_count-=1
        return max_length-1
