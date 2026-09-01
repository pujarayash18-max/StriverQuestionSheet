class Solution:
    def minInsertions(self, s):
        n = len(s)
        rev = s[::-1]

        # dp[i][j] = LCS length of
        # s[:i] and rev[:j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):

                if s[i - 1] == rev[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        # LCS length = Longest Palindromic Subsequence length
        lps = dp[n][n]

        # Characters not belonging to LPS need insertions
        return n - lps