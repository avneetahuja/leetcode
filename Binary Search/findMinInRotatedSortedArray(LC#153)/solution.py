class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if nums[l]<=nums[r]:
            return nums[0]
        while l<=r:
            m=l+(r-l)//2
            if nums[m]<nums[m-1]:
                return nums[m]
            elif nums[r]<nums[m]:
                l=m+1
            else:
                r=m-1
