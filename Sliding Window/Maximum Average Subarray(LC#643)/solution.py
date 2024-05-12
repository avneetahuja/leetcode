class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -float('inf')
        l,r,n,cur_sum = 0,0,len(nums),0

        while r<n:
            if r-l+1 <k:
                cur_sum+=nums[r]
                r+=1
            else:
                cur_sum+=nums[r]
                max_sum = max(max_sum,cur_sum)
                r+=1
                cur_sum-=nums[l]
                l+=1
        return max_sum/k
