'''
WA
3
'''
class Solution:
    # first, sollst du wissen's, k any ist.
    # ¡¡¡gesah ist one-dimension genug.
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        # dp[0] = 1
        # dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i - 1):
                # see when a single j, and whether
                # (i - j) is decomposed or not
                dp[i] = max(dp[i], j * (i - j), j *dp[i - j])  #### is j not dp[j]
        return dp[n]