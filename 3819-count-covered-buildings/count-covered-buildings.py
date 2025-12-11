class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        maxrow = [0] * (n + 1)
        minrow = [n + 1] * (n + 1)
        maxcol = [0] * (n + 1)
        mincol = [n + 1] * (n + 1)

        for r,c in buildings:
            maxrow[c] = max(maxrow[c], r)
            minrow[c] = min(minrow[c], r)
            maxcol[r] = max(maxcol[r], c)
            mincol[r] = min(mincol[r], c)

        res = 0
        for r,c in buildings:
            if r > minrow[c] and r < maxrow[c] and c > mincol[r] and c < maxcol[r]:
                res +=1

        return res