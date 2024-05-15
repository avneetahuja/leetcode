## Find Difference Between Two Arrays

### Problem Statement

You are given two integer arrays `nums1` and `nums2`. You need to return a list of two lists:
1. The first list should contain all the unique elements from `nums1` that are not present in `nums2`.
2. The second list should contain all the unique elements from `nums2` that are not present in `nums1`.

Each element should appear in the results without duplicates.

### Approach

1. **Use Sets for Efficient Lookups**:
   - Convert both arrays into dictionaries to keep track of their elements.
   - Use sets to store the unique elements that are only in `nums1` and not in `nums2`, and vice versa.

2. **Populate Dictionaries**:
   - Populate dictionaries `values_1` and `values_2` with elements from `nums1` and `nums2` respectively.

3. **Identify Unique Elements**:
   - Traverse `nums1` and check if the element is not in `values_2`. If true, add it to `set1`.
   - Traverse `nums2` and check if the element is not in `values_1`. If true, add it to `set2`.

4. **Convert Sets to Lists**:
   - Convert `set1` and `set2` to lists and return them as the result.

### Solution Code

```python
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        values_1, values_2 = {}, {}
        set1 = set()
        set2 = set()
        
        # Populate the dictionaries with elements from nums1 and nums2
        for n in nums1:
            values_1[n] = n
        for n in nums2:
            values_2[n] = n
        
        # Find unique elements in nums1 that are not in nums2
        for n in nums1:
            if not n in values_2:
                set1.add(n)
        
        # Find unique elements in nums2 that are not in nums1
        for n in nums2:
            if not n in values_1:
                set2.add(n)
        
        # Convert sets to lists and return the result
        return [list(set1), list(set2)]
```

### Explanation

1. **Dictionary Population**:
   - We populate `values_1` with elements from `nums1` and `values_2` with elements from `nums2`. This helps us to quickly check for the presence of elements from one list in the other.

2. **Set Population**:
   - We iterate through `nums1` and for each element, if it is not found in `values_2`, we add it to `set1`.
   - We iterate through `nums2` and for each element, if it is not found in `values_1`, we add it to `set2`.

3. **Return Result**:
   - We convert both `set1` and `set2` to lists and return them as the final result.

### Time Complexity

- The time complexity of this solution is O(n + m), where n is the length of `nums1` and m is the length of `nums2`. This is because we perform linear time operations to populate the dictionaries and sets.

### Space Complexity

- The space complexity is O(n + m) as we store elements from both `nums1` and `nums2` in dictionaries and sets.

This solution efficiently finds the unique elements from both lists using dictionaries and sets for quick lookups and ensures no duplicates in the final result.
