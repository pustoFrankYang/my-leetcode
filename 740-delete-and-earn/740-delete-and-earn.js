/**
 * @param {number[]} nums
 * @return {number}
 */
// WA: [1];;; [1,1,1,2,4,5,5,5,6]
var deleteAndEarn = function(nums) {
    if (nums.length == 1) return nums[0];  ////
    let n2pt = new Map();
    for (num of nums)
        if (n2pt.has(num))
            n2pt.set(num, n2pt.get(num) + num);
        else
            n2pt.set(num, num);
    let ns = [...n2pt.keys()];
    ns = ns.sort((a, b) => a - b);  // caution grammar
    let dp = new Array(ns.length);
    dp[0] = n2pt.get(ns[0]);
    dp[1] = ns[1] - ns[0] <= 1? Math.max(n2pt.get(ns[0]), n2pt.get(ns[1])) : n2pt.get(ns[1]) + dp[0];  ////
    for (let i = 2; i < ns.length; i ++) {
        if (ns[i] - ns[i - 1] <= 1)  ////
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + n2pt.get(ns[i]));
        else
            dp[i] = dp[i - 1] + n2pt.get(ns[i])
    }
    return dp[dp.length - 1];
};