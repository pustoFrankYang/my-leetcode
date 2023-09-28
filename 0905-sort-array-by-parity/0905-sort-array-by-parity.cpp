class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> ans(nums.size());
        int p = 0, q = nums.size() - 1;
        for (auto num : nums) {
            if (num % 2 == 0) {
                ans[p++] = num;
            } else {
                ans[q--] = num;
            }
        }
        return ans;
    }
};