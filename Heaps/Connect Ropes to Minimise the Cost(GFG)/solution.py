import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heap = [] 
        heapq.heapify(heap)
        for r in arr:
            heapq.heappush(heap,r)
        total = 0
        while len(heap)!=1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            total+=a+b
            heapq.heappush(heap,a+b)
        return total
