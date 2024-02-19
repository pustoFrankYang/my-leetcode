class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n == 1) return true;
        long long curr = 2;
        for (int i = 0; i < 31; i++) {
            if (n == curr) return true;
            curr *= 2;
        }
        return false;
    }
};