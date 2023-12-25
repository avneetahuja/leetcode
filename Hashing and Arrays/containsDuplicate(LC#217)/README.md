# Contains Duplicate 🔄

## Problem Statement

Given an array of integers `nums`, find if the array contains any duplicates. Your function should return `True` if any value appears at least twice in the array, and it should return `False` if every element is distinct.

**Example:**
Input: [1,2,3,1]
Output: True

Input: [1,2,3,4]
Output: False

Input: [1,1,1,3,3,4,3,2,4,2]
Output: True

## Approach 🛠️

I've used a Python class-based solution to check for duplicates in the given array.

1. I initialized an empty dictionary called `seen` to keep track of unique elements encountered so far.
2. I iterated through the array `nums`.
3. For each element `i` in `nums`, I checked whether it's already in the `seen` dictionary.
    - If it is, I returned `True` since it means the element is a duplicate.
    - If it's not, I added the element to the `seen` dictionary.
4. If the loop completes without finding any duplicates, I returned `False`.

## Complexity Analysis ⚙️

- Time Complexity: O(n) where n is the length of the input array `nums`.
  - The algorithm iterates through each element once.
- Space Complexity: O(n) where n is the length of the input array `nums`.
  - The space used by the `seen` dictionary is proportional to the number of unique elements in `nums`.
