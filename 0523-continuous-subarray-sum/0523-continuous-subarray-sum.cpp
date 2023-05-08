#include <unordered_map>
class Solution {
public:
    // gesah 一个评论区的小提示
    // 一个区间的和可以表示成两个累加和的差
    // 并结合取模运算
    bool checkSubarraySum(vector<int>& nums, int k) {
        // 此余数曾在何处出现。为了保证至少2元素
        // 初始化
        unordered_map<int, int> m{{0, -1}};
        int curr_sum = 0;
        for (int i = 0; i < nums.size(); i ++) {
            curr_sum = (curr_sum + nums[i]) % k;
            if (m.find(curr_sum) != m.end()) {
                if (m[curr_sum] < i - 1) return true;
            } else // don't update the idx when it is already in map!
                m[curr_sum] = i;
        }
        return false;
    }
};