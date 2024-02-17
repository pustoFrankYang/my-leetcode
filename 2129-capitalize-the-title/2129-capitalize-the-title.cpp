class Solution {
public:
    string capitalizeTitle(string title) {
        stringstream ss;
        ss << title;
        string word;
        string ans;
        while (ss >> word) {
            // 用来让单词之间加空格，且最后一个单词后没有，第一个单词前没有
            if (ans.size()) ans += ' ';
            
            if (word.size() <= 2) {
                transform(word.begin(), word.end(), word.begin(), ::tolower);
            } else {
                transform(word.begin(), word.end(), word.begin(), ::tolower);
                transform(word.begin(), word.begin() + 1, word.begin(), ::toupper);
            }
            ans += word;
        }
        return ans;
    }
};