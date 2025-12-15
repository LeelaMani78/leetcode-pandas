from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        streak = 0

        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                streak += 1
            else:
                streak = 1
            res += streak

        return res
