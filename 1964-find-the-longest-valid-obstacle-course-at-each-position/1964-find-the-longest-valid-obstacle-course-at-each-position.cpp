#include <algorithm>
class Solution {
public:
    vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
        int n = obstacles.size();
        // as in 300m,
        // d for last element of LIS of length i
        vector<int> ans(n, 1), d;
        for (int i = 0; i < n; i ++) {
            // use upper_bound instead of lower_bound
            // cuz elements in the course can equal
            int idx = upper_bound(d.begin(), d.end(), obstacles[i]) - d.begin();
            if (idx >= d.size())
                d.push_back(obstacles[i]);
            else
                d[idx] = obstacles[i];
            ans[i] = idx + 1;
        }
        return ans;
    }
};