# Network Delay Time ⏰

## Problem Statement

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given times, a list of travel times as directed edges `times[i] = (u, v, w)`, where `u` is the source node, `v` is the target node, and `w` is the time it takes for a signal to travel from source to target. We will send a signal from a given node `k`. Return the time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## Approach 🌟

To find the time it takes for all nodes to receive the signal, we can use Dijkstra's algorithm. The steps are as follows:

1. Build a graph representation from the given `times` list. We can use a dictionary of lists to store the edges, where the keys represent the source nodes and the values represent a list of tuples `(time, destination)` for each outgoing edge from that node.
2. Initialize a priority queue (`pq`) with the starting node `k` and a time of `0`.
3. Initialize an array `signal_received_times` to store the minimum time it takes for each node to receive the signal. Initialize all entries with infinity except for `k`, which should be set to `0`.
4. While the priority queue is not empty, do the following:
    - Pop the node with the minimum time (`cur_time`) from the priority queue.
    - If the current time (`cur_time`) for this node is greater than the time already stored in `signal_received_times[cur_node]`, continue to the next iteration (this node has already been visited with a shorter time).
    - Update the `signal_received_times` for the current node with `cur_time`.
    - Iterate through the neighbors of the current node, updating their arrival times in the `signal_received_times` array if the new time is smaller. Add them to the priority queue.
5. Finally, find the maximum value in the `signal_received_times`. If any node's arrival time is still infinity, return `-1` to indicate that the signal did not reach all nodes; otherwise, return the maximum arrival time.

## Complexity Analysis ⚙️

- Time Complexity: O(N log N + E), where N is the number of nodes and E is the number of edges (times).
  - Building the graph takes O(E) time.
  - Dijkstra's algorithm using a priority queue has a time complexity of O(N log N + E).
- Space Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
  - Additional space is required for the graph representation, priority queue, and the `signal_received_times` array.
