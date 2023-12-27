class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            l,r=i+1,len(nums)-1
            while(l<r):
                threesome = nums[i] + nums[l] + nums[r]
                if threesome == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while(nums[l]==nums[l-1]) and l<r:
                        l+=1
                elif threesome>0:
                    r-=1
                else:
                    l+=1
        return res
