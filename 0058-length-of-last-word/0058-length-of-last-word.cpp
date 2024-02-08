class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        string word;
        string last_word;
        while (ss >> word) {
            last_word = word;
        }
        return last_word.size();
    }
};