// ¡¡¡gesah

// We can split the array only if the score of all subarrays is zero.
// If the score of the entire array is not zero but m, then the score of any subarray cannot be less than m. Therefore, any split will add at least m to the sum.
// So, we count subarrays with the zero score.
// 惟全元素之位和为0时，方可split
// 因为，若全元素按位求和为m，其子序列位和亦至少m，
//     则一split至少使总和增m，不复最小
// 是故找零和者以为子序列

// 不过，为什么从头遍历，遇0则止，即是最大分割数？
class Solution {
public:
    int maxSubarrays(vector<int>& nums) {
        int res = 0, cur = INT_MAX;
        for (int n : nums) {
            cur &= n;
            if (cur == 0) {
                ++res;
                cur = INT_MAX;
            }
        }
        return max(1, res);
    }
};