class Solution {
public:
    double myPow(double x, int n) {
        int sign = n >= 0? 1 : -1;
        // ！！！直接在这一步把x改成倒数就可以了！！！以减少除法！！！
        if (sign < 0) {
            x = 1 / x;
        }
        // -2^31 取负数会超过 int 范围故
        // 注意 cpp 类型转换，需要在右边就转好
        unsigned int power = (unsigned int)sign * n;
        
        // 需要弄一个快速求幂的算法，才能省时间
        // 以后再想优化去掉递归
        // 就是 myPow(x * x, power / 2) 而不是 myPow(x, power / 2) * myPow(x, power / 2) 哦，不然怎么减少运算次数呢
        //double ans = 1;
        if (x == 1 || power == 1) {
            return x;
        } else if (power == 0) {
            // 不要忘了可能是0次幂！
            return 1;
        } else if (power % 2 == 1) {
            return x * myPow(x * x, power / 2);
        } else {
            return myPow(x * x, power / 2);
        }
        //return ans;
    }
};