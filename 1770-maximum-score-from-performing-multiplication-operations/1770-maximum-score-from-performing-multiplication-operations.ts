// Q1770m, runtime 87.50%, TS
function maximumScore(nums: number[], multipliers: number[]): number {
    var n = nums.length, m = multipliers.length;
    var dp = [] as number[][];
    for (let i = 0; i < m + 1; i ++) {
        dp.push(new Array(m + 1).fill(0));
    }
    for (let op = m - 1; op > -1; op --)
        for (let l = 0; l < op + 1; l ++) {
            let r = n - 1 - op + l;
            dp[l][op] = Math.max(
                multipliers[op] * nums[l] + dp[l + 1][op + 1],
                multipliers[op] * nums[r] + dp[l][op + 1]
            )
        }
    return dp[0][0];
};