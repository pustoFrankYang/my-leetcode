class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int curr = 0;
        vector<vector<int>> ans(n, vector<int> (n, 0));
        for (int i = 0; i < (n + 1) / 2; i ++) {
            for (int c = i; c < n - i; c ++)
                ans[i][c] = ++curr;
            for (int r = i + 1; r < n - i; r ++)
                ans[r][n - i - 1] = ++curr;
            if (curr >= n * n) break;
            for (int c = n - i - 2; c >= i; c --)
                ans[n - i - 1][c] = ++curr;
            for (int r = n - i - 2; r > i; r --)
                ans[r][i] = ++ curr;
        }
        return ans;
    }
};