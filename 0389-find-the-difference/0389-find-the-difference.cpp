class Solution {
public:
    char findTheDifference(string s, string t) {
        int cnts[26], cntt[26];
        memset(cnts, 0, sizeof(cnts));
        memset(cntt, 0, sizeof(cntt));
        for (const char& ch : s) {
            ++cnts[ch - 'a'];
        }
        for (const char& ch : t) {
            ++cntt[ch - 'a'];
        }
        
        for (int i = 0; i < 26; ++i) {
            if (cnts[i] != cntt[i])
                return char(i + 'a');
        }
        return 'x';
    }
};