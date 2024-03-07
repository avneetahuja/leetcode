class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        v = [-1] * len(cost)
        def f(i):
            if i==0 or i==1:
                return cost[i]
            if v[i] != -1:
                return v[i]
            else:
                v[i] = cost[i]+ min(f(i-1),f(i-2))
            return v[i]
        return min(f(len(cost)-1),f(len(cost)-2))
