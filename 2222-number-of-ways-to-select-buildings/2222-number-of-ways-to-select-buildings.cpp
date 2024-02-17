// !!! 只是把自己以前写的代码转成cpp观察一下
// 代码「翻译」的效果一般还不错，但是还是会有的case过不去



#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    long long numberOfWays(string s) {
        int n = s.size();
        
        vector<long long> pre0(n), pre1(n), suf0(n), suf1(n);
        long long ans = 0;
        
        for (int i = 0; i < n; ++i) {
            if (i == 0) {
                if (s[i] == '0') {
                    pre0[i] += 1;
                } else {
                    pre1[i] += 1;
                }
            } else {
                if (s[i] == '0') {
                    pre0[i] = pre0[i - 1] + 1;
                    pre1[i] = pre1[i - 1];
                } else {
                    pre1[i] = pre1[i - 1] + 1;
                    pre0[i] = pre0[i - 1];
                }
            }
        }
        
        for (int i = n - 1; i >= 0; --i) {
            if (i == n - 1) {
                if (s[i] == '0') {
                    suf0[i] += 1;
                } else {
                    suf1[i] += 1;
                }
            } else {
                if (s[i] == '0') {
                    suf0[i] = suf0[i + 1] + 1;
                    suf1[i] = suf1[i + 1];
                } else {
                    suf1[i] = suf1[i + 1] + 1;
                    suf0[i] = suf0[i + 1];
                }
            }
        }
        
        for (int i = 0; i < n; ++i) {
            if (s[i] == '0') {
                ans += pre1[i] * suf1[i];
            } else {
                ans += pre0[i] * suf0[i];
            }
        }
        
        return ans;
    }
};
