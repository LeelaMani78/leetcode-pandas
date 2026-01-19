from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Prefix sum: ps[i+1][j+1] = sum of mat[0..i][0..j]
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_sum = 0
            for j in range(n):
                row_sum += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

        def square_sum(r: int, c: int, k: int) -> int:
            # sum of submatrix with top-left (r,c) and side k
            r2, c2 = r + k, c + k
            return ps[r2][c2] - ps[r][c2] - ps[r2][c] + ps[r][c]

        # Check if there exists any k x k square with sum <= threshold
        def ok(k: int) -> bool:
            if k == 0:
                return True
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if square_sum(i, j, k) <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
