# Maximum Gold Collection

## Problem Statement

Given a 2D grid `grid` representing a gold mine. Each cell in this mine contains an integer representing the amount of gold in that cell. You start at the entrance of the mine. Each move, you can move to the left, right, up, or down. You can't visit the same cell more than once. You can start collecting gold from any position. If you have some amount of gold, you can move to a cell with gold adjacent to that cell and collect that gold. You can stop collecting gold anytime. Return the maximum amount of gold you can collect.

## Approach 🌟

We can use Depth-First Search (DFS) to explore all possible paths and compute the maximum amount of gold collected. We start DFS from each cell containing gold and recursively explore all possible directions. During the exploration, we keep track of the current sum of gold collected and update the maximum sum encountered so far.

1. Define a DFS function that takes the current position `(i, j)`, the current sum of gold collected, and a set of visited positions.
2. If the current position `(i, j)` is already visited, return the current sum of gold collected.
3. Add the gold in the current cell to the current sum and mark `(i, j)` as visited.
4. Explore all four directions from the current position `(i, j)` and recursively call DFS for each valid neighbor.
5. During the DFS exploration, keep track of the maximum sum of gold encountered.
6. Return the maximum sum of gold collected.

## Complexity Analysis ⚙️

- Time Complexity: O(R * C * 4^k), where R and C are the number of rows and columns in the grid, respectively, and k is the maximum length of any path in the grid. In the worst case, each cell can be visited multiple times during DFS exploration, resulting in a total of 4^k combinations.
- Space Complexity: O(R * C), where R and C are the number of rows and columns in the grid, respectively. We use a set to keep track of visited positions during DFS.
