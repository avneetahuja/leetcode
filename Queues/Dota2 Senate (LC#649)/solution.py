from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rCount = dCount = 0
        for senator in senate:
            if senator == 'R':
                rCount+=1
            else:
                dCount+=1
        rCurrentBanned = dCurrentBanned = 0
        q = collections.deque(senate)
        while not (rCount==0 or dCount==0):
            current = q.popleft()
            if current=='R':
                if rCurrentBanned>0:
                    rCurrentBanned-=1
                    rCount-=1
                else:
                    dCurrentBanned+=1
                    q.append(current)
            else:
                if dCurrentBanned > 0:
                    dCurrentBanned-=1
                    dCount-=1
                else:
                    rCurrentBanned+=1
                    q.append(current)
        return 'Radiant' if dCount==0 else 'Dire'
