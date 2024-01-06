class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if 0<m<len(nums)-1:
                if nums[m]==max(nums[m],nums[m-1],nums[m+1]):
                    return m
                elif nums[m+1]>nums[m]:
                    l=m+1
                else:
                    r=m-1
            elif m==0:
                if nums[m]>nums[m+1]:
                    return m
                else: 
                    return m+1
            else:
                if nums[m]>nums[m-1]:
                    return m
                else: 
                    return m-1
