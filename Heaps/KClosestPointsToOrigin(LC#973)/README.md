# K Closest Points to Origin 🎯

## Problem Statement

Given an array `points` representing coordinates of `n` points on a 2D plane, where `points[i] = [xi, yi]`, and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on a plane is the Euclidean distance.

The answer is guaranteed to be unique (except for the order that it is in).

## Approach 🚀

To find the `k` closest points to the origin, we can use a max-heap to maintain the `k` smallest distances from the origin. We'll iterate through each point in the input array `points`, calculate the distance of each point from the origin using the Euclidean distance formula, and store the negative of the distance along with the coordinates of the point in the max-heap.

### Steps:
1. Create a max-heap `heap`.
2. Iterate through each point `p` in the `points` array, and for each point do the following:
   - Calculate the squared Euclidean distance `d` of the point from the origin using the formula: `d = x^2 + y^2`.
   - Push the tuple `(-d, x, y)` onto the max-heap.
   - If the size of the max-heap exceeds `k`, pop the largest element.
3. After processing all points, extract the points from the max-heap and return them.

## Complexity Analysis ⚙️

- Time Complexity: O(N * log(K)), where N is the number of points and K is the given integer `k`.
  - Building the max-heap: O(N * log(K))
  - Extracting the result: O(K * log(K))
- Space Complexity: O(K)
  - The space is used to store the max-heap of size `k`.
