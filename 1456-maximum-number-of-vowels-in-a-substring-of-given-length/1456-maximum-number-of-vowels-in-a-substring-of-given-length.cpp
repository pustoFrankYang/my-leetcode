// C++复健, 试 LeetHub
class Solution {
public:
    bool isVowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
    }
    int maxVowels(string s, int k) {
        int p = 0, q = k - 1;
        int curr_cnt = 0, max_cnt = 0;
        for (int i = 0; i < k; i ++) {
            if (isVowel(s[i]))
                curr_cnt ++;
        }
        max_cnt = curr_cnt;
        while (q < s.length() - 1) {
            if (isVowel(s[p++])) curr_cnt --;
            if (isVowel(s[++q])) curr_cnt ++;
            if (max_cnt < curr_cnt) max_cnt = curr_cnt; 
        }
        return max_cnt;
    }
};