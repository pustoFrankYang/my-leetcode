class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // p: to add, q: examine, prev: prev q
        int p = 0, q = 0, prev = -10005, currcnt = 1;
        int n = nums.size();
        // 1 2 2 2 3 3 3 4
        // pq : currcnt = 1, update
        //   p q : currcnt = 1
        //   p   q : currcnt = 2
        for (int i = 0; i < n; i ++) {
            if (nums[q] != prev) {
                prev = nums[q];
                nums[p++] = nums[q++];
                currcnt = 1;
            } else {
                prev = nums[q];
                if (currcnt == 1) {
                    nums[p++] = nums[q++];
                    currcnt = 2;
                } else {
                    q++;
                }
            }
        }
        return p;
    }
};