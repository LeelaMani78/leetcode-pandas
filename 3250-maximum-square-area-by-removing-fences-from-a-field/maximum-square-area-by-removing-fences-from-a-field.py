class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7

        horizontals = set()
        verticals = set()

        hFences.extend([1, m])
        vFences.extend([1, n])

        hFences.sort()
        vFences.sort()

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                horizontals.add(hFences[j] - hFences[i])

        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                verticals.add(vFences[j] - vFences[i])

        res = 0
        for fence in horizontals:
            if fence in verticals:
                area = fence * fence
                res = max(res, area)

        return res % MOD if res != 0 else -1
