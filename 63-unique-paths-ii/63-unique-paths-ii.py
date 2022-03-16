class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i - 1][0] == 0 else 0
        for i in range(1, len(obstacleGrid[0])):
            dp[0][i] = dp[0][i - 1] if obstacleGrid[0][i - 1] == 0 else 0
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j - 1] == 0:
                    dp[i][j] += dp[i][j - 1]
                if obstacleGrid[i - 1][j] == 0:
                    dp[i][j] += dp[i - 1][j]
        return dp[-1][-1]