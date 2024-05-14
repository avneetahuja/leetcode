class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
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
        return max_length        
