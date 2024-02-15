class Solution:
    def zeroOneMemoized(self,weights,values,capacity,size):
        t = [[-1 for _ in range(capacity+1)] for _ in range(size+1)]

        def zeroOneKnapsack(weights,values,capacity,size):
            nonlocal t
            if size==0 or capacity==0:
                return 0
            if t[size][capacity]!=-1:
                return t[size][capacity]
            if weights[size-1]<=capacity:
                t[size][capacity]=max(values[size-1] + zeroOneKnapsack(weights,values,capacity-weights[-1],size-1),
                        zeroOneKnapsack(weights,values,capacity,size-1))
            else:
                t[size][capacity] = zeroOneKnapsack(weights,values,capacity,size-1)

            return t[size][capacity]

        return zeroOneKnapsack(weights,values,capacity,size)
    
            
s = Solution
print(s.zeroOneMemoized(s,weights=[1,2,4,5],values=[1,4,5,7],capacity=7,size=4))
