class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int sign = 0, len = nums.size();
        for (int i = 1; i < len; ++i) {
            int diff = nums[i] - nums[i - 1];
            int newsign = diff > 0? 1 : diff < 0? -1 : 0;
            if (sign == 0) {
                sign = newsign;
            } else if (newsign == 0) {
                continue;
            } else if (newsign != sign) {
                return false;
            }
        }
        return true;
    }
};