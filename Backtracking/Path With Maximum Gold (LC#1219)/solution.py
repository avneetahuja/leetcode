class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def dfs(i, j, current_value, visited):
            if (i, j) in visited:
                return current_value
            current_value += grid[i][j]
            visited.add((i, j))
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            max_gold = 0
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0 <= x < R and 0 <= y < C and grid[x][y] != 0:
                    max_gold = max(max_gold, dfs(x, y, 0, visited))
            visited.remove((i, j))
            return current_value + max_gold

        maximum = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] != 0:
                    cur = dfs(i, j, 0, set())
                    maximum = max(maximum, cur)
        return maximum
