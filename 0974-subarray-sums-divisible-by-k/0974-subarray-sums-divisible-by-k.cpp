#include <unordered_map>
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        unordered_map<int, int> m{{0, 1}};
        int ans = 0, curr_sum = 0;
        for (auto n : nums) {
            // !! avoid 取余的 negative res 
            curr_sum += n % k + k;
            curr_sum %= k;
            ans += m[curr_sum]++;
        }
        return ans;
    }
};