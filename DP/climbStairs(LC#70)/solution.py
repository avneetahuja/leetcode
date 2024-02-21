class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        prev2,prev,ans = 2,3,5
        for i in range(4,n+1):
            ans = prev+prev2
            prev2 = prev
            prev = ans
        return ans
