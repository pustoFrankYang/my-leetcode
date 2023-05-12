class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> dp(n, 0);
        for (int i = n - 1; i > -1; i --) {
            if (i == n - 1)
                dp[i] = questions[i][0];
            else if (questions[i][1] + i + 1 >= n)
                dp[i] = questions[i][0] > dp[i + 1] ? questions[i][0] : dp[i + 1];
            else
                dp[i] = questions[i][0] + dp[questions[i][1] + i + 1] > dp[i + 1] ?
                            questions[i][0] + dp[questions[i][1] + i + 1] :
                            dp[i + 1];
        }
        return dp[0];
    }
};