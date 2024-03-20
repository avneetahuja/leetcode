import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        s = 0
        heap =[]
        heapq.heapify(heap)
        for a in A:
            heapq.heappush(heap,a)
            if len(heap)>N-K1:
                heapq.heappop(heap)
        for i in range(K2-K1-1):
            s+=heapq.heappop(heap)
        return s
