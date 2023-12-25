# Product of Array Except Self 🔄

## Problem Statement

Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Example:**
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]

## Approach 🛠️

I've used a Python class-based solution to find the product of array elements except self.

1. I initialized a result list `res` with the same length as the input array `nums` and filled it with 1s.
2. I calculated the prefix product for each element in `nums` and stored it in the `res` list up to that index.
3. I then calculated the postfix product for each element in `nums` and multiplied it with the corresponding element in the `res` list.
4. The result is the product of all elements in the array except the current element.

## Complexity Analysis ⚙️

- Time Complexity: O(N), where N is the length of the input array `nums`.
  - The algorithm iterates through the input array twice, calculating the prefix and postfix products.
- Space Complexity: O(1), excluding the output array.
  - The algorithm uses a single result array to store the intermediate results.
