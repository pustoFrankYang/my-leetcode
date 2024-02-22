class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<bool> trusts_sb(n + 1);
        vector<int> cnt_trusted(n + 1);
        for (const auto& a2b : trust) {
            trusts_sb[a2b[0]] = true;
            cnt_trusted[a2b[1] ] ++;
        }
        for (int i = 1; i <= n; i++) {
            if (trusts_sb[i] == false && cnt_trusted[i] == n - 1) {
                return i;
            }
        }
        return -1;
    }
};