class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        if amount==0:
            return 0
        t = [[1000000 if i==0 else 0 for j in range(amount+1)] for i in range(n+1)]
        for i in range(1,amount+1):
            t[1][i] = 1000000 if i%coins[0]!=0 else i/coins[0]
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    t[i][j] = min(1+t[i][j-coins[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][amount] if t[n][amount] != 1000000 else -1
