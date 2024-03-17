import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while(len(stones)>1):
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            heapq.heappush(stones,first-second)
        return -stones[0]
