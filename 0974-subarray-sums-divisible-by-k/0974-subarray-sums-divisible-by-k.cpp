#include <unordered_map>
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> m{{0, 1}};
        int ans = 0, curr_sum = 0;
        for (auto n : nums) {
            curr_sum += n + k * 10000;
            curr_sum %= k;
            ans += m[curr_sum]++;
        }
        return ans;
    }
};