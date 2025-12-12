class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key = lambda e:e[0], reverse = True)
        events.sort(key = lambda e: int(e[1]))
        count = [0] * numberOfUsers
        returnTime = [0] * numberOfUsers

        for event in events:
            time = int(event[1])
            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                    for i in range(numberOfUsers):
                        count[i] +=1
                elif event[2] == "HERE":
                    for i, t in enumerate(returnTime):
                        if t <= time:
                            count[i] += 1
                else:
                    for index in event[2].split():
                        count[int(index[2:])] +=1
            
            else:
                    returnTime[int(event[2])] = time + 60
        return count            
                


        