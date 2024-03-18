
import heapq

class Solution:
    def nearlySorted(self,a,n,k):
        
        i,j = 0,k
        heap = a[i:j+1]
        heapq.heapify(heap)
        while j<n:
            a[i] = heapq.heappop(heap)
            j+=1
            i+=1
            if j == n:
                break
            heapq.heappush(heap,a[j])
            
        while i<n:
            a[i] = heapq.heappop(heap)
            i+=1
        return a
        
