class Solution:
    def firstNegativeOfSlidingWindow(self,nums,k):
        listt,res = [],[]
        i,j = 0,0
        while j<len(nums):
            if(nums[j]<0):
                listt.append(nums[j])
            if (j-i+1<k):
                j+=1
            elif (j-i+1==k):
                if(len(listt)==0):
                    res.append(0)
                else:
                    res.append(listt[0])
                    if nums[i] == listt[0]:
                        listt = listt[1:]
                i+=1
                j+=1
        return res
