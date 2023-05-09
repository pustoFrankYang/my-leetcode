class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size(), curr = 0;
        vector<int> ans(m*n, 0);
        for (int i = 0; i < (m > n ? n + 1 : m + 1)/2; i ++) {
            for (int c = i; c < n - i; c ++)
                ans[curr++] = matrix[i][c];
            for (int r = i + 1; r < m - i; r ++)
                ans[curr++] = matrix[r][n - i - 1];
            // avoid back and rewrite the last col/row
            if (curr >= ans.size()) break;
            for (int c = n - i - 2; c >= i; c --)
                ans[curr++] = matrix[m - i - 1][c];
            if (curr >= ans.size()) break;
            for (int r = m - i - 2; r > i; r --)
                ans[curr++] = matrix[r][i];
        }
        return ans;
    }
};