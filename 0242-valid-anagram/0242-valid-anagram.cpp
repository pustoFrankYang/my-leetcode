class Solution {
public:
    bool isAnagram(string s, string t) {
        int lens = s.size(), lent = t.size();
        if (lens != lent) return false;
        int cnts[26], cntt[26];
        memset(cnts, 0, sizeof(cnts));
        memset(cntt, 0, sizeof(cntt));
        for (int i = 0; i < lens; ++i) {
            ++cnts[s[i] - 'a'];
            ++cntt[t[i] - 'a'];
        }
        for (int i = 0; i < 26; ++i) {
            if (cnts[i] != cntt[i]) return false;
        }
        return true;
    }
};