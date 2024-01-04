class Solution:
  def countRotations(self,nums):
    l,r=0,0
    if(nums[0]<nums[len(nums)-1):
      return 0
    while(l<=r):
      mid=l+(r-l)//2
      if nums[mid-1]>nums[mid]:
        return mid
      elif nums[l]<=nums[mid]:
        l=mid+1
      else:
        r=mid-1
