class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // how to approach with bit manipulation?
        // we know: if there are 0-n 0-n with one x missing
        // then the 2n+1 numbers XOR each other
        // and here, the corresponding is index 0~n-1 and 0,n with x missing
        
        int x = nums.size();
        for (int i = 0; i < nums.size(); i++) {
            x = (i ^ nums[i]) ^ x;
        }
        return x;
    }
};