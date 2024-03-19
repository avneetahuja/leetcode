#code
import heapq

def freqSort(arr,n):
    heap = []
    map ={}
    for n in arr:
        map[n] = map.get(n,0)-1
    for key,value in map.items():
        heapq.heappush(heap,(value,key))
    li = []
    for h in heap:
        for n in range(-h[0]):
            li.append(h[1])
    return li
