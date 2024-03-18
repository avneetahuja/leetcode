import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        for n in arr:
            heapq.heappush(heap,(-abs(x-n),-n))
            if len(heap)>k:
                heapq.heappop(heap)
        li = []
        for i in range(len(heap)):
            li.append(-heap[i][1])
        li.sort()
        return li
