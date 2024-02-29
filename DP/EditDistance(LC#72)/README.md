# Edit Distance 👩‍💻📏

## Problem Statement

Given two strings `x` and `y`, find the minimum number of operations required to convert `x` to `y`. The allowed operations are:

1. Insert a character
2. Delete a character
3. Replace a character

## Approach 🛠️

We can solve this problem using dynamic programming. Let's define a 2D array `t` where `t[m][n]` represents the minimum number of operations required to convert `x[:n+1]` to `y[:m+1]`.

We can formulate our approach using the following recurrence relation:

- If `x[n] == y[m]`, then `t[m][n] = t[m-1][n-1]`.
  - This is because if the current characters match, no extra operation is needed.
- If `x[n] != y[m]`, then `t[m][n] = 1 + min(t[m-1][n], t[m-1][n-1], t[m][n-1])`.
  - This is because if the current characters don't match, we have three choices:
    1. Delete the character in `x` (corresponds to `t[m-1][n]`).
    2. Replace the character in `x` (corresponds to `t[m-1][n-1]`).
    3. Insert a character in `x` (corresponds to `t[m][n-1]`).

## Complexity Analysis ⚙️

- Time Complexity: O(len(x) * len(y))
  - We fill up the 2D array `t` of size len(y) * len(x).
- Space Complexity: O(len(x) * len(y))
  - We use a 2D array `t` for dynamic programming.
