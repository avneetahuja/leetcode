#Assuming nums is sorted
class Solution:
  def floorAndCeilingOfElement(self,nums,target):
    l,r=0,len(nums)-1
    while l<=r:
      m=l+(r-l)//2
      if nums[m]==target:
        return [nums[mid],nums[mid]]
      elif nums[m]<target:
        l=m+1
      else:
        r=m-1
    return [nums[l],nums[r]]
