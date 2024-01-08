class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,minIndex=0,len(nums)-1,-1
        if nums[l]<nums[r]:
            minIndex=0
        else:
            while l<=r:
                m=l+(r-l)//2
                if nums[m]==target:
                    return m
                if nums[m]<nums[m-1]:
                    minIndex=m
                    break
                elif nums[m]<nums[r]:
                    r=m-1
                else:
                    l=m+1
        l,r=0,minIndex-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        l,r=minIndex,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return -1
