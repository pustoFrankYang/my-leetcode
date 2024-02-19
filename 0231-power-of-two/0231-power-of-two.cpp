class Solution {
public:
    bool isPowerOfTwo(int n) {
        // 用位运算来解的话
        // 我一开始想错了，想成它是 111111 了，其实是 1000000啊。。。
        // 然后用题解里面学到的位运算的规律，与最后一个 1 的位有关的
        if (n <= 0) return false;
        long long x = n;
        // return (x & (x - 1)) == 0;
        return (x & (-x)) == x;
    }
};