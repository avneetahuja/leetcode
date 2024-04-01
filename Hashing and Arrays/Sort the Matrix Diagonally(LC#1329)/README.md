# Diagonal Sort 🔄

## Problem Statement

You are given an `m x n` matrix `mat` consisting of integers. You need to sort each diagonal in ascending order and return the resulting matrix.

A diagonal of a matrix `mat` is defined by a group of elements where row index `i` and column index `j` have the same value `i - j`.

## Approach 🔄

To solve this problem, we can follow these steps:
1. Iterate through each row `r` of the matrix `mat`.
    - Initialize variables `i` and `j` to `r` and `0`, respectively.
    - Initialize an empty list `arr` to store elements of the diagonal.
    - While `i` is less than the number of rows `R` and `j` is less than the number of columns `C`, append `mat[i][j]` to `arr` and increment `i` and `j`.
    - Sort the list `arr` in ascending order.
    - Reset `i` and `j` to `r` and `0`, respectively.
    - While `i` is less than `R` and `j` is less than `C`, assign `mat[i][j]` the values from the sorted list `arr` and increment `i` and `j`.
2. Iterate through each column `c` of the matrix `mat` except for the first column.
    - Initialize variables `i` and `j` to `0` and `c`, respectively.
    - Initialize an empty list `arr` to store elements of the diagonal.
    - While `i` is less than `R` and `j` is less than `C`, append `mat[i][j]` to `arr` and increment `i` and `j`.
    - Sort the list `arr` in ascending order.
    - Reset `i` and `j` to `0` and `c`, respectively.
    - While `i` is less than `R` and `j` is less than `C`, assign `mat[i][j]` the values from the sorted list `arr` and increment `i` and `j`.
3. Return the modified matrix `mat`.

## Complexity Analysis ⚙️

- Time Complexity: O(m * n * log(min(m, n)))
  - We traverse each diagonal once, where the maximum length of the diagonal is min(m, n). Sorting each diagonal takes O(min(m, n) * log(min(m, n))) time.
- Space Complexity: O(min(m, n))
  - We use extra space to store elements of each diagonal.
