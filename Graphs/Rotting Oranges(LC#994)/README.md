# Rotting Oranges 🍊🦠

## Problem Statement

You are given a grid representing the positions of oranges in a supermarket. Oranges are represented by the integer `1`, rotten oranges by `2`, and empty cells by `0`. Oranges adjacent to a rotten orange will also become rotten after one minute. Determine the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

## Approach 🍊🕰️

This problem can be solved using breadth-first search (BFS) to simulate the rotting process:

1. Initialize a queue `q` to store the positions of rotten oranges.
2. Count the number of fresh oranges (`ones`) in the grid.
3. Enqueue the positions of all rotten oranges into the queue.
4. Use a variable `time` to keep track of the minutes elapsed.
5. Define the directions to check for adjacent oranges: up, down, left, and right.
6. While the queue is not empty:
   - For each rotten orange in the queue:
     - Remove the current orange from the queue and mark it as visited.
     - Check all four directions for adjacent fresh oranges:
       - If found, mark the adjacent fresh orange as rotten, decrement the `ones` count, and enqueue its position.
   - Increment the `time` by 1 after processing all oranges in the current minute.
7. If there are no fresh oranges left (`ones == 0`), return the time minus 1 (as the initial state is considered minute 0).
8. If there are still fresh oranges left after processing, return `-1` indicating it's impossible to rot all oranges.

## Complexity Analysis ⚙️

- Time Complexity: O(R * C)
  - Each cell of the grid is visited at most once in the worst case.
- Space Complexity: O(R * C)
  - The space used by the queue can be up to the size of the grid.
