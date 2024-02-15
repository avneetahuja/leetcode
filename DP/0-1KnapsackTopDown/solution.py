class Solution:
    def zeroOneTopDown(self,weights,values,capacity,size):
        t = [[0 if i == 0 or j == 0 else -1 for j in range(capacity + 1)] for i in range(size + 1)]
        for i in range(1,size+1):
            for j in range(1,capacity+1):
                if weights[i-1]<=j:
                    t[i][j] = max(values[i-1]+t[i-1][j-weights[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        print(t)
        return t[size][capacity]
    
            
s = Solution
print(s.zeroOneTopDown(s,weights=[1,2,4,5],values=[1,4,5,7],capacity=7,size=4))
