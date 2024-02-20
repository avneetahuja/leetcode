class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s1 = (sum(nums)+target)//2
        n=len(nums)
        t = [[0 for i in range(s1+1)] for j in range(n+1)]
        for i in range(n+1):
            t[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,s1+1):
                if t[i][j]<=j:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][s1]

        
