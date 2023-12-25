class Solution:
    def maxSumSubarrayOfSizeK(self,nums,k):
        i,j,sum,maxSum=0,0,0,0
        while j< len(nums):
            sum+=nums[j]
            if(j-i+1<k):
                j+=1
            elif j-i+1==k:
                maxSum = max(maxSum,sum)
                sum-=nums[i]
                i+=1
                j+=1
        return maxSum
