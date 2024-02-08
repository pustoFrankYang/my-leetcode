class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        // try if another way can quicker
        bool increasing = true, decreasing = true;
        int len = nums.size();
        for (int i = 1; i < len; ++i) {
            if (nums[i] > nums[i - 1]) {
                decreasing = false;
            } 
            if (nums[i] < nums[i - 1]) {
                increasing = false;
            } 
        }
        return increasing || decreasing;
    }
};