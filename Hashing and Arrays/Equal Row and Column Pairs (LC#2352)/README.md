# Equal Row and Column Pairs

## Problem Statement
Given a 2D grid of integers, count the number of pairs (R, C) such that row R is identical to column C.

## Approach

### Steps

1. **Count Row Occurrences**:
   - Use a dictionary to count the occurrences of each row in the grid.
   
2. **Check Columns**:
   - Iterate through each column of the grid.
   - Convert each column into a tuple and check if this tuple exists in the row dictionary.
   - If it exists, increment the count by the number of times the row appears.

### Solution Code

```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}        
        count = 0
        n = len(grid)
        
        for row in grid:
            rows[tuple(row)] = 1 + rows.get(tuple(row), 0)
        
        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            if tuple(col) in rows:
                count += rows[tuple(col)]
                
        return count
```

### Explanation

1. **Counting Row Occurrences**:
   - Convert each row of the grid into a tuple (to use as a dictionary key).
   - Populate the `rows` dictionary with the count of each row tuple.

2. **Checking Columns**:
   - Iterate over each column index.
   - For each column, create a list of elements in that column.
   - Convert this column list into a tuple.
   - Check if this column tuple exists in the `rows` dictionary.
   - If it exists, increment the `count` by the value associated with this tuple in the dictionary.

### Time Complexity
- The time complexity of this solution is O(n^2), where n is the length of the grid. This is due to the two nested loops: one for iterating over rows and another for iterating over columns.

### Space Complexity
- The space complexity is O(n^2) due to the storage of rows and columns as tuples in the dictionary.
