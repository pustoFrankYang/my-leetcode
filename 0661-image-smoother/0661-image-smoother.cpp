class Solution {
public:
    inline bool isValid(int ni, int nj, int isize, int jsize) {
        return ni >= 0 && ni < isize && nj >= 0 && nj < jsize;
    }
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        vector<pair<int, int>> dirs = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1}, {0, 0}, {0, 1},
            {1, -1}, {1, 0}, {1, 1},
        };
        vector<vector<int>> ans(img.size(), vector<int>(img[0].size()));
        for (int i = 0; i < img.size(); i++) {
            for (int j = 0; j < img[0].size(); j++) {
                int accu = 0, cnt = 0;
                for (const auto& dir : dirs) {
                    int ni = i + dir.first, nj = j + dir.second;
                    if (isValid(ni, nj, img.size(), img[0].size())) {
                        accu += img[ni][nj];
                        cnt ++;
                    }
                }
                ans[i][j] = accu / cnt;
            }
        }
        return ans;
    }
};