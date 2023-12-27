# 3Sum 3️⃣🏥

## Problem Statement

Given an array of integers `nums`, find all unique triplets in the array that sum up to zero.

**Example:**
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

## Approach 🛠️

I've used a two-pointer approach to find unique triplets that sum up to zero, similar to the approach used in the `twoSum` problem with a sorted array.

1. I sorted the array `nums` to make the two-pointer approach feasible.
2. I initialized an empty list `res` to store the unique triplets.
3. I iterated through the sorted array using a for loop.
4. For each element at index `i`, I used two pointers `l` and `r` to search for a pair of numbers that sum up to the negative of `nums[i]`.
5. I handled duplicates by skipping identical elements using `if nums[i] == nums[i-1]`.
6. If a triplet is found, I added it to the result list `res`.
7. I adjusted the pointers based on the comparison of the triplet sum with zero.
8. The process continued until the pointers met.

## Complexity Analysis ⚙️

- Time Complexity: O(n^2), where n is the length of the input array `nums`.
  - The algorithm iterates through the array with two nested loops.
- Space Complexity: O(1) excluding the space needed for the output.
  - The algorithm uses a constant amount of space.
