class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // !!! 仅供观察用，原python答案自动转成C++
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> ans;

        for (int i = 0; i < nums.size() - 2; ++i) {
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            int l = i + 1, r = nums.size() - 1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] == 0) {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    ++l;
                    while (l < nums.size() && nums[l] == nums[l - 1]) {
                        ++l;
                    }
                    --r;
                    while (r >= 0 && nums[r] == nums[r + 1]) {
                        --r;
                    }
                } else if (nums[i] + nums[l] + nums[r] < 0) {
                    ++l;
                } else {
                    --r;
                }
            }
        }

        return ans;
    }
};