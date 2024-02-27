# Matrix Chain Multiplication 🔄✖️

## Problem Statement

Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide the sequence of the matrix multiplications involved.

## Approach 🛠️

To solve this problem, we can use dynamic programming. We'll create a recursive function to calculate the minimum number of multiplications needed for a given range of matrices, and we'll use memoization to avoid redundant calculations.

1. Initialize a memoization table `t` with dimensions `n x n`, where `n` is the number of matrices.
2. Define a recursive function `solve` to calculate the minimum number of multiplications needed for a range of matrices `[i, j]`.
3. In the `solve` function:
   - If `i` is equal to `j`, return 0 (no multiplication needed for a single matrix).
   - If the result for the range `[i, j]` is already memoized, return the memoized result.
   - Iterate through the possible split points `k` in the range `[i, j]`.
     - Calculate the number of multiplications needed for the left and right subproblems and the multiplication of the two resulting matrices.
     - Update the minimum number of multiplications.
   - Memoize the result for the current range `[i, j]`.
4. Return the result obtained from the `solve` function for the range `[1, n-1]`, where `n` is the number of matrices.

## Complexity Analysis ⚙️

- Time Complexity: O(n^2)
  - The solution involves a triple nested loop.
- Space Complexity: O(n^2)
  - Memoization table `t` with dimensions `n x n`.
