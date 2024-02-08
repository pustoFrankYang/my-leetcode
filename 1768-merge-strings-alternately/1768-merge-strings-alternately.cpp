class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int len1 = word1.size(), len2 = word2.size();
        int len_less = min(len1, len2);
        stringstream ss;
        for (int i = 0; i < len_less; ++i) {
            ss << word1[i] << word2[i];
        }
        ss << (len1 == len_less? word2.substr(len_less) : word1.substr(len_less));
        return ss.str();
    }
};