class Solution:
  def countNumberOfOccurencesInSortedList(self,nums,target):
    l,r,first,last=0,0,-1,-1
    while l<=r:
      m=l+(r-l)//2
      if nums[m]==target:
        first=m
        r=m-1
      elif nums[m]<target:
        l=m+1
      else:
        r=m-1
    l,r=0,0
    while l<=r:
      m=l+(r-l)//2
      if nums[m]==target:
        last=m
        l=m+1
      elif nums[m]<target:
        l=m+1
      else:
        r=m-1
    return last-first+1
