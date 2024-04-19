# Moving Zeroes

## Problem Statement

Given an array `nums`, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

**Example:**
Input: `[0,1,0,3,12]`
Output: `[1,3,12,0,0]`

## Approach 🌟

To move all the zeroes to the end of the array while maintaining the relative order of the non-zero elements, we can use a two-pointer approach.

1. Initialize two pointers `l` and `r` to track the current positions of the left and right elements, respectively.
2. Iterate through the array using the `l` pointer:
   - If `nums[l]` is equal to 0, find the next non-zero element using the `r` pointer.
   - Swap `nums[l]` with `nums[r]`.
   - Increment `l` to continue the iteration.
3. Repeat this process until `l` reaches the end of the array.
4. At the end of the iteration, all zeroes will be moved to the end of the array, while the relative order of the non-zero elements will be maintained.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the number of elements in the array.
  - We iterate through the array once.
- Space Complexity: O(1).
  - We use only a constant amount of extra space.
