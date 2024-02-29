# Interleaving String 🧵🔀

## Problem Statement

Given three strings `x`, `y`, and `z`, determine whether `z` can be formed by interleaving `x` and `y`. An interleaving of two strings preserves the order of characters from each string while merging them into a new string.

## Approach 🛤️

We can solve this problem using dynamic programming. Let's define a 2D array `t` where `t[m][n]` represents whether the first `m+1` characters of `x` and the first `n+1` characters of `y` can form the first `m+n+2` characters of `z`.

### Recurrence Relation:

- If `m < 0`, return `y[:n+1] == z[:m+1]`.
  - If there are no characters left in `x`, check if the remaining characters in `y` match the remaining characters in `z`.
- If `n < 0`, return `x[:m+1] == z[:n+1]`.
  - If there are no characters left in `y`, check if the remaining characters in `x` match the remaining characters in `z`.
- If `r < 0`, return `False`.
  - If there are no characters left in `z` but characters are remaining in both `x` and `y`, return `False`.

- If `x[m] == z[r]` and `y[n] == z[r]`, then `t[m][n] = f(m-1, n, r-1) or f(m, n-1, r-1)`.
  - This is because we can either choose a character from `x` or `y` to form the next character in `z`.
- If `x[m] == z[r]`, then `t[m][n] = f(m-1, n, r-1)`.
  - This is because we can only choose a character from `x` to form the next character in `z`.
- If `y[n] == z[r]`, then `t[m][n] = f(m, n-1, r-1)`.
  - This is because we can only choose a character from `y` to form the next character in `z`.

### Base Cases:

- If `m < 0`, return `y[:n+1] == z[:m+1]`.
  - If there are no characters left in `x`, check if the remaining characters in `y` match the remaining characters in `z`.
- If `n < 0`, return `x[:m+1] == z[:n+1]`.
  - If there are no characters left in `y`, check if the remaining characters in `x` match the remaining characters in `z`.
- If `r < 0`, return `True`.
  - If there are no characters left in `z`, the interleaving is successful.

## Complexity Analysis ⚙️

- Time Complexity: O(len(x) * len(y))
  - We fill up the 2D array `t` of size len(y) * len(x).
- Space Complexity: O(len(x) * len(y))
  - We use a 2D array `t` for dynamic programming.
