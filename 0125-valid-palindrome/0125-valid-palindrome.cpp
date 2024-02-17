class Solution {
public:
    bool isPalindrome(string s) {
        string tmp = "";
        for (const char& ch : s) {
            if (ch >= 'a' && ch <= 'z') {
                tmp += ch;
            } else if (ch >= 'A' && ch <= 'Z') {
                tmp += tolower(ch);
            } else if (ch >= '0' && ch <= '9') {
                // 我靠我忘了题干说了包括数字
                tmp += ch;
            }
        }
        int p = 0, q = tmp.size() - 1;
        
        while (p < q) {

            if (tmp[p++] != tmp[q--]) return false;
        }
        return true;
    }
};