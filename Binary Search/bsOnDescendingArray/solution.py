class Solution:
    def binarySearchDescending(self,nums,target):
      l,r=0,0
      while l<=r:
        mid = l+ (r-l)//2
        if nums[mid]==target:
          return mid
        elif nums[mid]>target:
          l=mid+1
        else:
          r=mid-1
      return -1
