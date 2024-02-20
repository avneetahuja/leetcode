class Solution:

    def rodCutting(length, prices):
        arr = [i+1 for i in range(length)]
        n = len(arr)
        t = [[0 for i in range(length+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,length+1):
                if arr[i-1]<=j:
                    t[i][j] = max(prices[i-1] + t[i][j-arr[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][length]
