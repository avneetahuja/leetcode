# Median of Two Sorted Arrays 📊

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

## Approach 🛠️

I've implemented an efficient algorithm using binary search to find the partition in the smaller array that ensures both left and right parts of the combined array have an equal number of elements.

1. I set `lSmall` and `rSmall` as the boundaries for the partition in the smaller array (`nums1`).
2. I calculate `mSmall` as the middle index in the partition of `nums1`.
3. I calculate `mBig` as the corresponding middle index in the partition of `nums2`.
4. I compare elements at indices `mSmall` and `mBig` with their adjacent elements to ensure the partition is correct.
5. If the partition is correct, I calculate the median based on the elements at the partition indices.
6. If the partition is not correct, I adjust the boundaries (`lSmall` or `rSmall`) accordingly based on the comparison results.

## Complexity Analysis ⚙️

- Time Complexity: O(log(min(m, n))), where `m` and `n` are the lengths of `nums1` and `nums2`.
- Space Complexity: O(1), as no extra space is used.

