# Longest Consecutive Sequence 📏

## Problem Statement

Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence.

A consecutive sequence is a sequence of integers where adjacent elements differ by exactly 1.

**Example:**
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, the length is 4.

## Approach 🛠️

I've used a Python class-based solution to find the length of the longest consecutive elements sequence.

1. I created a set `nSet` to store the unique elements from the input array `nums`.
2. I initialized a variable `maxL` to keep track of the maximum length of consecutive sequences.
3. I iterated through each element `n` in the `nSet`.
4. For each element, I checked if the previous element `(n-1)` is not in the set.
    - If not, I initiated a loop to find the length of the consecutive sequence starting from the current element `n`.
5. I incremented the length `l` while `(n + l)` is in the set.
6. I updated `maxL` with the maximum of the current `maxL` and `l`.
7. The function returned the maximum length of consecutive sequences.

## Complexity Analysis ⚙️

- Time Complexity: O(n), where n is the length of the input array `nums`.
  - The algorithm iterates through each element once.
- Space Complexity: O(n), where n is the length of the input array `nums`.
  - The space used by the `nSet` set.
