# Nested List Weighted Sum II

## Problem Statement

Given a nested list of integers, `nestedList`, where each element is either an integer or a list whose elements may also be integers or other lists, compute the sum of each integer in the list weighted by its depth. The weight of an integer is defined as the maximum depth of the list minus the depth of the integer plus 1.

## Approach

1. **Find Maximum Depth**:
   - Traverse the nested list to determine the maximum depth. This will help us calculate the weight of each integer.
   
2. **Calculate Weighted Sum**:
   - Using the maximum depth, compute the weighted sum of all integers in the nested list.
   - Traverse the nested list again, this time calculating the sum of each integer multiplied by its weight.

### Detailed Steps

1. **Finding Maximum Depth**:
   - Define a helper function `findMaxDepth` that takes a nested list and returns its maximum depth.
   - Traverse through each element of the list. If the element is an integer, continue. If the element is a list, recursively call `findMaxDepth` on that list and update the maximum depth accordingly.

2. **Finding Weighted Sum**:
   - Define another helper function `findWeightedSum` that takes a nested list, the current depth, and the maximum depth.
   - Traverse through each element of the list. If the element is an integer, calculate its weight based on the formula `max_D - depth + 1` and add the weighted integer to `depth_sum`. If the element is a list, recursively call `findWeightedSum` on that list with an incremented depth.

## Complexity

- **Time Complexity**: O(N), where N is the total number of integers and lists in the nested structure. This is because we traverse each element twice: once for finding the maximum depth and once for calculating the weighted sum.
- **Space Complexity**: O(D), where D is the maximum depth of the nested list. This accounts for the space used by the call stack during recursion.

## Solution Code

```python
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        depth_sum = 0

        def findMaxDepth(el):
            max_depth = 1
            for element in el:
                if not element.isInteger() and len(element.getList()) > 0:
                    max_depth = max(max_depth, 1 + findMaxDepth(element.getList()))
            return max_depth
        
        def findWeightedSum(li, depth, max_D):
            nonlocal depth_sum
            for element in li:
                if element.isInteger():
                    depth_sum += element.getInteger() * (max_D - depth + 1)
                elif len(element.getList()) > 0:
                    findWeightedSum(element.getList(), depth + 1, max_D)
        
        max_D = findMaxDepth(nestedList)
        findWeightedSum(nestedList, 1, max_D)
        return depth_sum
```

## Explanation

1. **findMaxDepth**:
   - Traverses the nested list to find the maximum depth.
   - Recursively calls itself for each nested list to determine the deepest level.

2. **findWeightedSum**:
   - Traverses the nested list to compute the weighted sum.
   - For each integer, calculates its weight based on the maximum depth and its current depth, and adds the weighted value to `depth_sum`.
   - Recursively calls itself for each nested list, incrementing the depth by 1.
