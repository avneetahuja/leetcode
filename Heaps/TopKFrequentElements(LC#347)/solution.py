import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        heap = []
        for n in nums:
            map[n] = 1+ map.get(n,0)
        heapq.heapify(heap)
        for key,val in map.items():
            heapq.heappush(heap,(val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        li = []
        for h in heap:
            li.append(h[1])
        return li
