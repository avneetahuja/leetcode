from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.stream = deque()
        self.size=size

    def next(self, val: int) -> float:
        self.stream.appendleft(val)
        if len(self.stream)>self.size:
            self.stream.pop()
        return sum(self.stream)/len(self.stream)
