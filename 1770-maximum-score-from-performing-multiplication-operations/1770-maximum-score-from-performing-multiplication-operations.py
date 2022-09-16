# Note: The python code of top-down DP may give Time Limit Exceeded/Memory Limit Exceeded since it has a larger constant factor.
# Q1770m, TLE or runtime 13.96%, py
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # l + (len (- 1) - r) = op; r = len - 1 - op + l
        # so states are l and op
        m, n = len(multipliers), len(nums)
        # dp[the left choice][number of operations done]
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][m] = 0
        for op in range(m - 1, -1, -1): # op reverse iter
            for l in range(op + 1): # l any order but must within op
                r = n - 1 - op + l
                dp[l][op] = max(
                    multipliers[op] * nums[l] + dp[l + 1][op + 1], 
                    multipliers[op] * nums[r] + dp[l][op + 1]
                               )
        return dp[0][0]