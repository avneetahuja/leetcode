# Check if Two Strings are Close

## Problem Statement
Two strings are considered close if you can attain one from the other using the following operations:
1. Swap any two existing characters.
2. Transform every occurrence of one existing character into another existing character, and do the same with the other character.

Given two strings `word1` and `word2`, return `True` if `word1` and `word2` are close, and `False` otherwise.

## Approach

### Steps

1. **Length Check**:
   - If the lengths of `word1` and `word2` are not equal, return `False` immediately, as they cannot be close.

2. **Count Frequencies**:
   - Use dictionaries to count the frequency of each character in both `word1` and `word2`.

3. **Compare Frequency Values and Keys**:
   - Check if the sorted lists of frequency values from both words are the same.
   - Check if the sorted lists of unique characters (keys) from both words are the same.
   - If both conditions are met, return `True`; otherwise, return `False`.

### Solution Code

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)
        if n != m:
            return False
        
        counts1, counts2 = {}, {}
        for c in word1:
            counts1[c] = 1 + counts1.get(c, 0)
        for c in word2:
            counts2[c] = 1 + counts2.get(c, 0)
        
        return sorted(counts1.values()) == sorted(counts2.values()) and sorted(counts1.keys()) == sorted(counts2.keys())
```
### Time Complexity
- The time complexity of this solution is O(n log n), where n is the length of the input strings. This is due to the sorting operations on the dictionary values and keys.

### Space Complexity
- The space complexity is O(n) for the additional dictionaries used to store character frequencies.
