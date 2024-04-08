# Minimum Cost to Connect All Points 🌐

## Problem Statement

You are given an array `points` representing the coordinates of points on a 2D plane. The cost of connecting any two points `i` and `j` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## Approach 🌟

To find the minimum cost to connect all points, we can use Kruskal's algorithm, which is a minimum spanning tree (MST) algorithm. The steps are as follows:

1. Calculate the Manhattan distance between each pair of points and store them along with their corresponding indices.
2. Sort the distances in ascending order.
3. Initialize a union-find data structure to keep track of the connected components.
4. Iterate through the sorted distances:
    - If adding the current edge does not create a cycle, add it to the MST and update the total cost.
5. Continue until all points are connected or we have added `n - 1` edges.
6. Return the total cost.

## Complexity Analysis ⚙️

- Time Complexity: O(N^2 log N), where N is the number of points.
  - Calculating the Manhattan distance between each pair of points takes O(N^2) time.
  - Sorting the distances takes O(N^2 log N) time.
  - Union-find operations take nearly constant time on average.
- Space Complexity: O(N), where N is the number of points.
  - Additional space is required for storing the distances and the union-find data structure.
