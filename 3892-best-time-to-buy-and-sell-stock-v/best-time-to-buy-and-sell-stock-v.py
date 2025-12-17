class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        # dp[i][t][s] - s = not holding | holding normal | holding short
        dp = [[[-inf] * 3 for t in range(k + 1)] for i in range(n)]
        dp[0][0][0] = 0 # skip day
        dp[0][0][1] = -prices[0] # open normal
        dp[0][0][2] = prices[0] # open short

        for i in range(1,n):
            for t in range(k + 1):
                # no changes
                dp[i][t][0] = dp[i - 1][t][0]
                dp[i][t][1] = dp[i - 1][t][1]
                dp[i][t][2] = dp[i - 1][t][2]

                dp[i][t][1] = max(dp[i][t][1], dp[i - 1][t][0] -prices[i]) # open normal
                dp[i][t][2] = max(dp[i][t][2],dp[i - 1][t][0] + prices[i]) # open short


                if t:
                    dp[i][t][0] = max(dp[i][t][0], dp[i - 1][t - 1][1] + prices[i]) # close normal
                    dp[i][t][0] = max(dp[i][t][0],dp[i - 1][t - 1][2] - prices[i]) # close short

        return max(dp[-1][t][0] for t in range(k + 1))
        