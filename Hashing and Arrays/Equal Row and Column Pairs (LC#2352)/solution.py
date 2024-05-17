class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows ={}        
        count = 0
        n = len(grid)
        for row in grid:
            rows[tuple(row)] = 1+ rows.get(tuple(row),0)
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            if tuple(col) in rows:
                count += rows[tuple(col)]
        return count
