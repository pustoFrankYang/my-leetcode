// ！！！！只是把几年前的答案重新提交观察一下
class Solution {
public:
    string longestPalindrome(string s) {
        int reslen=0, resbegin=0;
        if (!s.size()) return s;
        for (int i = 0; i < s.size(); i++) {
            int len = lengthOfPalinDavon(s, i, i);
            if (len >= reslen) {
                reslen = len;
                resbegin = i - len / 2;
            }
        }
        for (int i = 0; i < s.size() - 1; i++) {
            int len = lengthOfPalinDavon(s, i, i + 1);
            if (len >= reslen) {
                reslen = len;
                resbegin = i + 1 - len / 2;
            }
        }
        return s.substr(resbegin, reslen);
    }
    int lengthOfPalinDavon(string s,int coreL, int coreR) {
        //int res = 1;
        while (coreL>=0 && coreR < s.size() && s[coreL]==s[coreR]){
            //res = coreR - coreL + 1;
            coreL--;
            coreR++;
        }
        return coreR - coreL - 1;
    }
};