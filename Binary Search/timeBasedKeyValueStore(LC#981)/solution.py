class TimeMap:

    def __init__(self):
        self.map={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([value,timestamp])
        else:
            self.map[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        ans=""
        if key in self.map:
            l,r=0,len(self.map[key])-1
            if timestamp<self.map[key][0][1]:
                return ans
            while l<=r:

                m=l+(r-l)//2
                if self.map[key][m][1]==timestamp:
                    return self.map[key][m][0]
                elif self.map[key][m][1]<timestamp:
                    l=m+1
                else:
                    r=m-1
            
            ans=self.map[key][r][0]
        return ans
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
