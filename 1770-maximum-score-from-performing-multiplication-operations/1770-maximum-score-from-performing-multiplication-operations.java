// Q1770m, runtime 94.49%, java
class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        int m = multipliers.length, n = nums.length;
        int[][] dp = new int[m + 1][m + 1];
        for (int op = m - 1; op > -1; op --)
            for (int l = 0; l < op + 1; l ++) {
                int r = n - 1 - op + l;
                dp[l][op] = Math.max(
                    multipliers[op] * nums[l] + dp[l + 1][op + 1],
                    multipliers[op] * nums[r] + dp[l][op + 1]
                );
            }
        return dp[0][0];
    }
}