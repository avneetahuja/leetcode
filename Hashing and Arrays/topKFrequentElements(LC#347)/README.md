# Top K Frequent Elements 📊

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example:**
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

## Approach 🛠️

I've used a Python class-based solution to find the `k` most frequent elements in the array.

1. I initialized a dictionary called `count` to store the frequency of each element in the array.
2. I created a list called `freq` to represent the frequency buckets. Each index `i` in `freq` corresponds to a list of elements that occur `i` times.
3. I iterated through the array `nums` and updated the `count` dictionary.
4. I then iterated through the items in the `count` dictionary and populated the `freq` list with elements based on their frequencies.
5. Finally, I constructed the result list `res` by iterating through the `freq` list in reverse order (from higher frequencies to lower frequencies) until the first `k` elements are found.

## Complexity Analysis ⚙️

- Time Complexity: O(N + K), where N is the length of the input array `nums` and K is the value of `k`.
  - The algorithm iterates through each element in `nums` and the items in the `count` dictionary.
- Space Complexity: O(N), where N is the length of the input array `nums`.
  - The space used by the `count` dictionary and the `freq` list.
