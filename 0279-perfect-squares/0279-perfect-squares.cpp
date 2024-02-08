class Solution {
public:
    // O(100n) = O(n)
    int numSquares(int n) {
        // I guess we can use DP 
        // cuz you can get the result smh from smaller number
        // but seems not so straightforward...
        // alreadies hold itself == itself: dp[1], dp[4], dp[9]...
        // others can try dp[n] = dp[n - i] + dp[i]
        // but wherefrom the `i`?
        // check every squared numbers?
        // oh make sense cuz n <= 10000
        // vector<int> perfect_squares(101);
        // for (int i = 1; i <= 100; ++i) {
        //     perfect_squares[i] = i * i;
        // }
        
        // remember to init to int-max
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i <= n; ++i) {
            for (int j = 1; j * j <= i; ++j) {
                dp[i] = min(dp[i], 1 + dp[i - j * j]);
            }
        }
        
        return dp[n];
    }
};