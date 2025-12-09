class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y = defaultdict(int)
        mod = 10 ** 9 + 7
        res = 0
        total = 0

        for p in points:
            y[p[1]] +=1

        for p in y.values():
            edges = p*(p-1)//2
            res += edges * total
            total +=edges

        return res % mod
        