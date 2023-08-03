class Solution {
public:
    int nthUglyNumber(int n) {
        // ？？？竟然使用int，还真不能用 long long。为啥？
        vector<int> uHp = { 1 };
        unordered_set<int> set = { 1 };
        long long ans = 0;
        for (int i = 0; i < n; i ++) {
            ans = uHp[0];
            if (i == n - 1) return ans;
            pop_heap(uHp.begin(), uHp.end(), greater<int>());
            uHp.pop_back(); //
            if (ans*2 < INT_MAX && !set.contains(ans*2)) {
                uHp.push_back(ans*2);
                push_heap(uHp.begin(), uHp.end(), greater<int>());
                set.insert(ans*2);
            }
            if (ans*3 < INT_MAX && !set.contains(ans*3)) {
                uHp.push_back(ans*3);
                push_heap(uHp.begin(), uHp.end(), greater<int>());
                set.insert(ans*3);
            }
            if (ans*5 < INT_MAX && !set.contains(ans*5)) {
                uHp.push_back(ans*5);
                push_heap(uHp.begin(), uHp.end(), greater<int>());
                set.insert(ans*5);
            }
        }
        return (int)ans;
    }
};