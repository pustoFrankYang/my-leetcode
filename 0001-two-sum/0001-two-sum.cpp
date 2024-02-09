class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num2idx;
        int len = nums.size();
        for (int i = 0; i < len; ++i) {
            if (num2idx.find(target - nums[i]) != num2idx.end()) {
                return vector<int>{num2idx[target - nums[i]], i};
            }
            num2idx[nums[i]] = i;
        }
        return vector<int>{0, 0};
    }
};