class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<bool> row_is_zero(m, false), col_is_zero(n, false);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    row_is_zero[i] = true;
                    col_is_zero[j] = true;
                }
            }
        }
        for (int r = 0; r < m; ++r) {
            if (row_is_zero[r]) {
                for (int c = 0; c < n; ++c) {
                    matrix[r][c] = 0;
                }
            }
        }
        for (int c = 0; c < n; ++c) {
            if (col_is_zero[c]) {
                for (int r = 0; r < m; ++r) {
                    matrix[r][c] = 0;
                }
            }
        }
        return;
    }
};