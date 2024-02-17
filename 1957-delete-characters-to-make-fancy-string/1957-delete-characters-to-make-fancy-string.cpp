class Solution {
public:
    string makeFancyString(string s) {
        int curr = 1;
        string ans = "";
        ans += s[0];
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) {
                curr++;
                if (curr <= 2) {
                    ans += s[i];
                }
            } else {
                curr = 1;
                ans += s[i];
            }
        }
        return ans;
    }
};