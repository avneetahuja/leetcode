class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r,c = 0,len(nums)-1,0
        while l<r:
            if nums[l]+nums[r]<k:
                l+=1
            elif nums[l]+nums[r]>k:
                r-=1
            else:
                c+=1
                l+=1
                r-=1
        return c
