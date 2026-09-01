class Solution:
    def change(self, amount, coins):
        # dp[x] = number of combinations to make amount x
        dp = [0] * (amount + 1)

        # There is 1 way to make amount 0:
        # choose nothing
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]

        return dp[amount]