# Intuition
The problem requires finding the maximum time taken for a signal to reach all nodes in a network starting from a particular node. This can be solved efficiently using Dijkstra's algorithm.

# Approach
1. Construct an adjacency list representation of the graph.
2. Initialize a priority queue to hold nodes based on their signal arrival times.
3. Initialize an array to store the time at which each node receives the signal, initially set to infinity except for the source node which is set to 0.
4. Perform Dijkstra's algorithm:
   - Pop the node with the minimum signal arrival time from the priority queue.
   - Update the signal arrival time for its neighbors if a shorter path is found.
   - Push the updated nodes into the priority queue.
5. Finally, find the maximum signal arrival time among all nodes.

# Complexity
- Time complexity: O(E log V), where E is the number of edges and V is the number of vertices. This is due to the priority queue operations in Dijkstra's algorithm.
- Space complexity: O(V), where V is the number of vertices. This is due to the space required for storing the adjacency list and signal arrival times array.

# Code
```python
import collections
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Constructing adjacency list
        graph = collections.defaultdict(list)
        for edge in times:
            graph[edge[0]].append([edge[2], edge[1]])
        
        # Priority queue initialization with source node
        pq = [(0, k)]
        
        # Signal arrival times array initialization
        signal_received_times = [float('inf')] * (n + 1)
        signal_received_times[k] = 0
        
        # Dijkstra's algorithm
        while pq:
            cur_time, cur_node = heapq.heappop(pq)
            if cur_time > signal_received_times[cur_node]:
                continue
            for time, destination in graph[cur_node]:
                if time + cur_time < signal_received_times[destination]:
                    signal_received_times[destination] = time + cur_time
                    heapq.heappush(pq, (signal_received_times[destination], destination))
        
        # Finding maximum signal arrival time
        result = max(signal_received_times[1:])
        
        return result if result != float('inf') else -1
```
