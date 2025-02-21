class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * n  # Count of '*' up to each index
        left = [-1] * n  # Nearest left candle
        right = [-1] * n  # Nearest right candle
        
        # Compute prefix sum of '*'
        count = 0
        for i in range(n):
            if s[i] == '*':
                count += 1
            prefix[i] = count

        # Compute nearest left candle index
        nearest = -1
        for i in range(n):
            if s[i] == '|':
                nearest = i
            left[i] = nearest

        # Compute nearest right candle index
        nearest = -1
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                nearest = i
            right[i] = nearest

        # Answer queries using precomputed arrays
        ans = []
        for start, end in queries:
            l = right[start]  # First candle from start
            r = left[end]  # Last candle from end
            if l != -1 and r != -1 and l < r:
                ans.append(prefix[r] - prefix[l])
            else:
                ans.append(0)  # No valid range
        return ans
