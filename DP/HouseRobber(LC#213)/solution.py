class Solution:
    def rob(self, nums: List[int]) -> int:
        # def f(idx,flag):
        #     if idx<0:
        #         return 0
        #     if idx==0 and flag:
        #         return 0
        #     if idx == len(nums)-1:
        #         flag=True
        #     return max(f)
        # Own solution beat 91% LFGGGG
        if len(nums)<=1:
            return max(nums[0],0)
        n = len(nums)
        t = [[0 for i in range(2)] for j in range(n+1)]

        t[1][0] = nums[0]
        for i in range (2,n):
            for j in range(2):
                t[i][j] = max(nums[i-1]+t[i-2][j],t[i-1][j])
        t[n][0] = t[n-1][0]
        t[n][1] = max(nums[n-1]+t[n-2][1],t[n-1][1])
        return max(t[n][0],t[n][1])
