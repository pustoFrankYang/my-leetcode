#include <algorithm>
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        // last element of LIS of length i
        vector<int> d;
        for (int i = 0; i < n; i ++) {
            // use lower_bound, cuz:
            // lower_bound is the first equalled element
            // upper_bound is after the last equalled element
            int idx = lower_bound(d.begin(), d.end(), nums[i]) - d.begin();
            if (idx == d.size())
                d.push_back(nums[i]);
            else
                d[idx] = nums[i];
        }
        return d.size();
    }
};