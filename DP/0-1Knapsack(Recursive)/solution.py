class Solution:
    def zeroOneKnapsack(self,weights,values,capacity):
        if len(weights)==0 or capacity==0:
            return 0
        if weights[-1]<=capacity:
            return max(values[-1] + self.zeroOneKnapsack(self,weights[0:len(weights)-1],values[0:len(values)-1],capacity-weights[-1]),
                       self.zeroOneKnapsack(self,weights[0:len(weights)-1],values[0:len(values)-1],capacity))
        else:
            return self.zeroOneKnapsack(self,weights[0:len(weights)-1],values[0:len(values)-1],capacity)
