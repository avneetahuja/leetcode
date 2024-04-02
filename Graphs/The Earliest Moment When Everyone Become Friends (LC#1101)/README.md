# The Earliest Moment When Everyone Become Friends 🕒

## Problem Statement

You are given a list `logs`, where `logs[i] = [timestampi, personi, personj]` indicates that `personi` wants to form a connection with `personj` at time `timestampi`.

Return the earliest time at which all people will be in an extended friend circle.

If it's impossible, return `-1`.

## Approach 🌐

To solve this problem, we can use the Union-Find algorithm. We'll follow these steps:
1. Sort the `logs` array based on the timestamp in ascending order.
2. Initialize an array `root` of size `n`, where `root[i]` represents the parent of node `i` initially set to `i`.
3. Initialize an array `rank` of size `n`, where `rank[i]` represents the rank (depth) of the subtree rooted at node `i`, initially set to `1`.
4. Initialize a variable `c` to `n`, which represents the number of connected components.
5. Define a function `find(i)` to find the root of the component containing node `i`. If `root[i]` is not equal to `i`, recursively find the root of the component containing the parent of node `i`.
6. Define a function `union(i, j)` to union the components containing nodes `i` and `j`. If the roots of `i` and `j` are not the same, merge the smaller rank tree into the larger rank tree. If the ranks are equal, choose any tree and increment its rank. Decrement `c` after the union operation.
7. Iterate through each log in `logs`. For each log, union the components containing the persons involved. Check if `c` becomes `1` after each union operation. If `c` becomes `1`, return the timestamp of the current log.
8. If all persons are not in the same connected component after processing all logs, return `-1`.

## Complexity Analysis ⚙️

- Time Complexity: O(nlogn + nα(n)), where `n` is the number of logs and `α(n)` is the inverse Ackermann function.
  - Sorting the logs array takes O(nlogn) time.
  - The Union-Find operations take nearly constant time per operation due to path compression and union by rank.
- Space Complexity: O(n)
  - We use extra space to store the parent array and rank array.
