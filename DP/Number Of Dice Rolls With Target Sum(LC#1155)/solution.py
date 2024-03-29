class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        t = {} 
        def f(nLeft, s):
            if nLeft == 0:
                return 1 if s == 0 else 0
            if (nLeft, s) in t:
                return t[(nLeft, s)]
            t[(nLeft, s)] = 0
            for i in range(1, k + 1): 
                if s - i >= 0:
                    t[(nLeft, s)] += f(nLeft - 1, s - i)
            return t[(nLeft, s)]
        return f(n, target) % (10**9 + 7)
