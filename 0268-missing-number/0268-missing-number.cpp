class Solution {
public:
    int missingNumber(vector<int>& nums) {
        vector<bool> has(nums.size() + 1);
        for (int i = 0; i < nums.size(); i ++) {
            has[nums[i]] = true;
        }
        for (int i = 0; i <= nums.size(); i ++) {
            if (!has[i]) return i;
        }
        return 0;
    }
};