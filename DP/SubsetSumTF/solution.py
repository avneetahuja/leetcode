class Solution:
    def subSumPresent(self,arr,sum):
        t = [[False for j in range(sum+1)] for i in range(len(arr)+1)]
        for i in range(len(arr)+1):
            t[i][0] = True
       
        for i in range(1,len(arr)+1):
            for j in range(1,sum+1):
                if arr[i-1]<=j:
                    t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]
        print(t)
        return t[len(arr)][sum]

s = Solution()
print(s.subSumPresent([0,1,2,3],3))
