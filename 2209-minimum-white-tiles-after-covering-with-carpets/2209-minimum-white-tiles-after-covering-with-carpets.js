/**
 * @param {string} floor
 * @param {number} numCarpets
 * @param {number} carpetLen
 * @return {number}
 */
// ¡¡¡¡gesah
var minimumWhiteTiles = function(floor, numCarpets, carpetLen) {
    let dp = Array.from(Array(floor.length + 1), () => new Array(numCarpets + 1).fill(0));
    for (let i = 1; i <= floor.length; i ++)
        for (let j = 0; j <= numCarpets; j ++) {
            let noNew = floor[i - 1] == '1' ? dp[i - 1][j] + 1 : dp[i - 1][j];
            let newCarp = j > 0 ? dp[Math.max(0, i - carpetLen)][j - 1] : 1005;
            dp[i][j] = Math.min(noNew, newCarp);
        }
    return dp[floor.length][numCarpets];
};