#This is just one of the approaches, you can increase r by an even greater factor ofcourse
class Solution:
  def findIndexInInfiniteArray(self,nums,target):
    l,r=0,100
    while(nums[r]<target):
      l=r
      r=r**r
    while l<=r:
      m=l+(r-l)//2
      if nums[m]==target:
        return m
      elif nums[m]<target:
        l=m+1
      else:
        r=m-1
    return -1
