class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        prev2=0
        prev=1
        ans = 0
        for i in range(2,n+1):
            ans = prev+prev2
            prev2 = prev
            prev = ans
        return ans
