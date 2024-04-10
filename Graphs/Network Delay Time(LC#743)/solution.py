import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        pq = [(0,k)]
        for edge in times:
            graph[edge[0]].append([edge[2],edge[1]])
        signal_received_times = [float('inf')]*(n+1)
        signal_received_times[k] = 0
        while pq:
            cur_time,cur_node = heapq.heappop(pq)
            if cur_time > signal_received_times[cur_node]:
                continue
            for time, destination in graph[cur_node]:
                if time + cur_time < signal_received_times[destination]:
                    signal_received_times[destination] = time + cur_time
                    heapq.heappush(pq,(signal_received_times[destination],destination))

        result = max(signal_received_times[1:])

        return result if result != float('inf') else -1
