class Solution {
public:
    int arraySign(vector<int>& nums) {
        int res = 1;
        for (const int& num : nums) {
            if (num == 0) {
                return 0;
            } else if (num < 0) {
                res = -res;
            }
        }
        return res;
    }
};