from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        prefix_sell = [0]
        prefix = [0]

        for p, s in zip(prices, strategy):
            prefix.append(prefix[-1] + p * s)
            prefix_sell.append(prefix_sell[-1] + p)

        N = len(prices)
        total = prefix[-1]
        best = total

        for i in range(N):
            if i + k <= N:
                best = max(
                    best,
                    total
                    - (prefix[i + k] - prefix[i])
                    + (prefix_sell[i + k] - prefix_sell[i + k // 2])
                )

        return best
