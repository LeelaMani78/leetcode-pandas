class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        times = []

        for e in events:
            times.append([e[0], "begin",e[2]])
            times.append([e[1],  "end",e[2]])

        res = 0
        maxval = 0
        times.sort()

        for e in times:
            if e[1] == "begin":
               res = max(res,e[2] + maxval)
            else:
                maxval = max(maxval,e[2])

        return res
        