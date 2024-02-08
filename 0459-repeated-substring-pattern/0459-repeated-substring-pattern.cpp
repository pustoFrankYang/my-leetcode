class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int len = s.length();
        for (int i = len - 1; i > 0; --i) {
            if (len % i != 0) {
                continue;
            }
            string repeated = "";
            string substr = s.substr(0, i);
            for (int j = 0; j < len / i; ++j) {
                repeated += substr;
            }
            if (repeated == s) return true;
        }
        return false;
    }
};