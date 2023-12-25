class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        listt = []
        i,j=0,0
        res=[]
        while j<len(nums):
            while len(listt)>0 and listt[len(listt)-1]<nums[j]:
                listt = listt[0:len(listt)-1]
            listt.append(nums[j])
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                res.append(listt[0])
                if(listt[0]==nums[i]):
                    listt= listt[1:]
                i+=1
                j+=1
        return res
