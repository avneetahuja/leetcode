class Solution:
    def largestSubarrayOfSumK(self,nums,k):
        i,j,s,maxL = 0,0,0,0
        while(j<len(nums)):
            s+=nums[j]
            if(s<k):
                j+=1
            elif s==k:
                if j-i+1>maxL:
                    maxL = j-i+1
                j+=1
            else:
                while s>k:
                    s-=nums[i]
                    i+=1
                j+=1
        return maxL
