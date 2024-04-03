# Smallest String With Swaps 🔄

## Problem Statement

You are given a string `s`, and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates two indices `(0-indexed)` of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that `s` can be changed to after using the swaps.

## Approach 🌟

To solve this problem, we can use a union-find algorithm combined with sorting. Here's the approach:

1. Initialize a `root` array of size `n` and a `rank` array of size `n`, where `n` is the length of string `s`. The `root[i]` represents the parent of node `i`, initially set to `i`. The `rank[i]` represents the rank (depth) of the subtree rooted at node `i`, initially set to `1`.
2. Define a function `find(i)` to find the root of the component containing node `i`. If `root[i]` is not equal to `i`, recursively find the root of the component containing the parent of node `i`. Apply path compression during the find operation.
3. Define a function `union(i, j)` to union the components containing nodes `i` and `j`. If the roots of `i` and `j` are not the same, merge the smaller rank tree into the larger rank tree. If the ranks are equal, choose any tree and increment its rank.
4. Iterate through each pair in `pairs` and union the components containing the indices in each pair.
5. Create a dictionary `roots` to store the root nodes and their corresponding indices in the string.
6. Iterate through each root in `roots`. For each root, extract the characters corresponding to its indices in the string, sort them lexicographically, and update the string with the sorted characters.
7. Return the modified string `s`.

## Complexity Analysis ⚙️

- Time Complexity: O(nlogn + nα(n)), where `n` is the length of the string `s` and `α(n)` is the inverse Ackermann function.
  - Sorting the characters for each connected component takes O(nlogn) time.
  - The Union-Find operations take nearly constant time per operation due to path compression and union by rank.
- Space Complexity: O(n)
  - We use extra space to store the parent array, rank array, and the `roots` dictionary.
