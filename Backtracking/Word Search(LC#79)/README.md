# Word Search 🕵️‍♂️🔍

## Problem Statement

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Note:**
- You can assume all inputs consist of lowercase letters a-z.

## Approach 🚀

This problem can be solved using a Depth-First Search (DFS) approach. We can start the search from each cell that matches the first character of the word and explore its neighboring cells recursively.

### Steps:
1. Initialize a set `visited` to keep track of visited cells.
2. Define a recursive function `search(i, j, ind)` that explores cells starting from the given indices `(i, j)` and considering the character at position `ind` in the word.
3. In the `search` function:
   - Check if the current cell `(i, j)` is already visited. If yes, return `False`.
   - Check if the character at the current cell matches the character at position `ind` in the word. If not, return `False`.
   - Check if `ind` is equal to the length of the word. If yes, return `True` (word is found).
   - Mark the current cell as visited by adding `(i, j)` to the `visited` set.
   - Recursively explore neighboring cells in all four directions (up, down, left, right) by calling `search` with updated indices and `ind+1`.
   - Unmark the current cell by removing `(i, j)` from the `visited` set before returning from the function.
4. Iterate over all cells in the board and start the search from each cell that matches the first character of the word.
5. If the search from any starting cell returns `True`, return `True`. Otherwise, return `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(N * M * 4^L), where N is the number of rows, M is the number of columns, and L is the length of the word.
  - The DFS explores neighboring cells in all four directions, and there are 4^L possible paths for each starting cell.
- Space Complexity: O(L), where L is the length of the word.
  - The space is used for the `visited` set and the recursive call stack during DFS.
