# Two Sum II - Input Array is Sorted 🎯

## Problem Statement

Given an array of integers `numbers` that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function should return an array containing indices of the two numbers where each index is 1-based and must not be the same.

You may assume that each input would have exactly one solution and you may not use the same element twice.

**Example:**
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, the indices are 1 and 2.

## Approach 🛠️

I've used a two-pointer approach to find the indices of the two numbers in the sorted array.

1. I initialized two pointers `p1` and `p2` at the beginning and end of the array, respectively.
2. I used a while loop to iterate through the array until `p1` is less than `p2`.
3. I calculated the sum `s` of the numbers at indices `p1` and `p2`.
4. If `s` is equal to the target, I returned the indices `[p1 + 1, p2 + 1]` since the indices are 1-based.
5. If `s` is less than the target, I incremented `p1` to move towards larger numbers.
6. If `s` is greater than the target, I decremented `p2` to move towards smaller numbers.
7. If no pair is found, the function returned `-1`.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `numbers`.
  - The algorithm iterates through the array once using the two-pointer approach.
- Space Complexity: O(1).
  - The algorithm uses a constant amount of space.
