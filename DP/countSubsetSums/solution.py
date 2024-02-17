class Solution:
    def countSumSubsets(self,arr,sum):
        t = [[False for j in range(sum+1)] for i in range(len(arr)+1)]
        count=0
        for i in range(len(arr)+1):
            t[i][0] = True
       
        for i in range(1,len(arr)+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
                
        for i in range(len(arr)+1):
            if t[i][sum]:
                count+=1
        return count

s = Solution()
print(s.countSumSubsets([0,1,2,3,4,6],6))
