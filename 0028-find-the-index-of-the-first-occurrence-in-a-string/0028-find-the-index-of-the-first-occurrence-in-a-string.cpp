class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t idx = haystack.find(needle);
        if (idx != string::npos) {
            return idx;
        } else {
            return -1;
        }
    }
};