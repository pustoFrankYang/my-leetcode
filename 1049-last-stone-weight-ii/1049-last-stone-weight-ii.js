/**
 * @param {number[]} stones
 * @return {number}
 */
// https://github.com/youngyangyang04/leetcode-master/blob/master/problems/1049.%E6%9C%80%E5%90%8E%E4%B8%80%E5%9D%97%E7%9F%B3%E5%A4%B4%E7%9A%84%E9%87%8D%E9%87%8FII.md
// ¡¡¡gesah!!! ???? wow du kannst aber...
// zwei Gruppen, und Gruppe 0 nur smash nach stone in Gruppe 1
// als ob ein Gruppe ein Sum ist
var lastStoneWeightII = function(stones) {
    let dp = Array(1501).fill(0);  // not 1500!!! cuz you want dp[1500]
    let target = stones.reduce((a, b) => a + b, 0);
    target = Math.floor(target / 2);
    for (let i = 0; i < stones.length; i ++) {
        for (let j = target; j >= stones[i]; j --) {
            dp[j] = Math.max(dp[j], dp[j - stones[i]] + stones[i])
        }
    }
    return stones.reduce((a, b) => a + b, 0) - dp[target] - dp[target];
};