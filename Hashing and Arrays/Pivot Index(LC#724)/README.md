## Pivot Index

### Problem Statement

The pivot index of an array is the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index. Given an array of integers `nums`, return the pivot index. If no such index exists, return -1. If there are multiple pivot indices, return the left-most pivot index.

### Approach

1. **Calculate Left and Right Sums**:
   - Use two arrays `lSum` and `rSum` to store the cumulative sums of elements to the left and right of each index, respectively.
   
2. **Compute Cumulative Sums**:
   - Populate `lSum` such that `lSum[i]` contains the sum of elements from the start up to but not including index `i`.
   - Populate `rSum` such that `rSum[i]` contains the sum of elements from index `i+1` to the end.

3. **Find Pivot Index**:
   - Iterate through the array and find the index where `lSum[i]` is equal to `rSum[i]`.

### Time Complexity

- The time complexity is O(n) where n is the length of the input array, since we traverse the array three times: once to fill `lSum`, once to fill `rSum`, and once to find the pivot index.

### Space Complexity

- The space complexity is O(n) due to the additional space needed for the `lSum` and `rSum` arrays.

### Solution Code

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        lSum = [0] * n
        rSum = [0] * n
        
        # Calculate left sum array
        for i in range(1, n):
            lSum[i] = lSum[i - 1] + nums[i - 1]
        
        # Calculate right sum array
        for i in range(n - 2, -1, -1):
            rSum[i] = rSum[i + 1] + nums[i + 1]
        
        # Find the pivot index
        for i in range(n):
            if lSum[i] == rSum[i]:
                return i
                
        return -1
```

### Explanation

1. **Left Sum Calculation**:
   - For each index `i`, `lSum[i]` stores the sum of all elements to the left of `i`. This is done by adding the current element to the previous left sum.
   
2. **Right Sum Calculation**:
   - For each index `i`, `rSum[i]` stores the sum of all elements to the right of `i`. This is done by adding the current element to the next right sum.

3. **Pivot Index Search**:
   - We iterate through each index and check if the left sum is equal to the right sum. If they are equal, the current index is the pivot index.

4. **Return**:
   - If no pivot index is found where the left sum equals the right sum, return `-1`.

This solution ensures that we correctly identify the pivot index by maintaining the sums of elements on either side of each index in linear time.
