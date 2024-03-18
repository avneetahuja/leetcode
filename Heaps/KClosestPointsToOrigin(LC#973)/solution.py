import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(points)):
            d = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            heapq.heappush(heap, (-d, points[i][0], points[i][1]))
            if len(heap)>k:
                heapq.heappop(heap)
        li =[]
        for point in heap:
            li.append([point[1],point[2]])
        return li
        
