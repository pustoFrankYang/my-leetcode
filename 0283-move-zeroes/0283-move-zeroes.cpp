class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int p = 0, q = 0;
        int len = nums.size();
        while (q < len) {
            if (nums[q] != 0) {
                nums[p++] = nums[q];
            }
            ++q;
        }
        while (p < len) {
            nums[p++] = 0;
        } 
    }
};