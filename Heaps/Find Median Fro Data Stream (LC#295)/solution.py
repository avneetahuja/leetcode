class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        heapq.heapify(self.small_heap)
        heapq.heapify(self.large_heap)


    def addNum(self, num: int) -> None:
        
        if not self.small_heap and not self.large_heap:
            heapq.heappush(self.large_heap,num)
        elif len(self.small_heap) > len(self.large_heap):
            if num >= self.large_heap[0] or num>-self.small_heap[0]:
                heapq.heappush(self.large_heap,num)
            else:
                element = heapq.heappop(self.small_heap)
                heapq.heappush(self.large_heap,-element)
                heapq.heappush(self.small_heap,-num)
        elif len(self.small_heap) == len(self.large_heap):
            if num >= self.large_heap[0]:
                heapq.heappush(self.large_heap,num)
            else:
                heapq.heappush(self.small_heap,-num)
        elif len(self.small_heap) < len(self.large_heap):
            if num >= self.large_heap[0]:
                element = heapq.heappop(self.large_heap)
                heapq.heappush(self.large_heap,num)
                heapq.heappush(self.small_heap,-element)
            else:
                heapq.heappush(self.small_heap,-num)
        # print()
        # print(self.small_heap,self.large_heap, num)
        # print(self.findMedian())
        # print()


    def findMedian(self) -> float:
        # if not self.small_heap:
        #     return self.large_heap[0]
        if (len(self.small_heap) + len(self.large_heap))%2==0:
            return (-self.small_heap[0]+self.large_heap[0])/2
        if len(self.small_heap)>len(self.large_heap):
            return -self.small_heap[0]
        if len(self.small_heap)<len(self.large_heap):
            return self.large_heap[0]
        return "FAIL" 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
