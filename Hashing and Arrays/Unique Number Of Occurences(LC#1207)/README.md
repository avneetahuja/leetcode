# Unique Number of Occurrences

## Problem Statement
Given an array of integers `arr`, return `True` if the number of occurrences of each value in the array is unique. Otherwise, return `False`.

## Approach

### Steps

1. **Count Frequencies**:
   - Traverse through the array and count the frequency of each number using a dictionary (`counts`).

2. **Check Uniqueness of Frequencies**:
   - Use another dictionary (`values`) to track the frequencies.
   - Traverse through the values of the `counts` dictionary and check if each frequency is unique by verifying its existence in the `values` dictionary.
   - If any frequency is found more than once, return `False`.

3. **Return the Result**:
   - If all frequencies are unique, return `True`.

### Solution Code

```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for n in arr:
            counts[n] = 1 + counts.get(n, 0)
        values = {}
        for n in counts.values():
            if n in values:
                return False
            values[n] = n
        return True
```

### Time Complexity
- The time complexity of this solution is O(n), where n is the length of `arr`. This is because we traverse the array and the dictionary values only once.

### Space Complexity
- The space complexity is O(n) as we use dictionaries to store counts and track unique frequencies.
