class Solution {
public:
    bool isPalindrome(const string& str) {
        int p = 0, q = str.size() - 1;
        while (p < q) {
            if (str[p++] != str[q--]) {
                return false;
            }
        }
        return true;
    }
    string firstPalindrome(vector<string>& words) {
        for (const string& word : words) {
            if (isPalindrome(word)) {
                return word;
            }
        }
        return "";
    }
};