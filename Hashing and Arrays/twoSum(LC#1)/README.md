# Two Sum 🎯

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] equals 9, so the output is [0, 1].

## Approach 🛠️

I've used a Python class-based solution that employs a dictionary to store the complement of each number as we iterate through the array.

1. I initialized an empty dictionary called `comps` to store the complements.
2. I iterated through the array `nums` using both the element `n` and its index `i`.
3. For each element `n`, I calculated its complement as `target - n`.
4. I checked if the complement is already in the `comps` dictionary.
   - If it is, I found a pair, and I returned the indices `[i, comps[comp]]`.
   - If not, I added the current element and its index to the `comps` dictionary.
5. If the loop completes without finding a pair, it means there's no valid solution.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through each element once.
- Space Complexity: O(n), where n is the length of the input array `nums`.
  - The space used by the `comps` dictionary is proportional to the number of elements in `nums`.
