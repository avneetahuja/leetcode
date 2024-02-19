class Solution:
    def countSubsetsWithGivenDifference(self,arr,target):
        s1 = (target+sum(arr))//2
        t = [[0 for j in range(s1+1)] for i in range(len(arr)+1)]
        count=0
        for i in range(len(arr)+1):
            t[i][0] = 1
       
        for i in range(1,len(arr)+1):
            for j in range(1,s1+1):
                if arr[i-1]<=j:
                    t[i][j] = t[i-1][j-arr[i-1]] + t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        print(t)
        return t[len(arr)][s1]

s = Solution()
print(s.countSubsetsWithGivenDifference([1,1,2,3],1))
