# Search a 2D Matrix 🔍🔢

## Problem Statement

You are given a 2D matrix where:
- Each row is sorted in ascending order.
- The first integer of each row is greater than the last integer of the previous row.

You are also given a target integer. Your task is to determine if the target is present in the matrix.

## Approach 🛠️

I've implemented a binary search-based approach to efficiently search the matrix.

1. I performed binary search on the first column of the matrix to determine the potential row where the target might be present.
2. Once the potential row is found, I performed another binary search on that row to check if the target is present.

## Complexity Analysis ⚙️

- Time Complexity: O(log(m) + log(n)), where m is the number of rows and n is the number of columns.
  - The first binary search is performed on the rows, and the second binary search is performed on the columns.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
