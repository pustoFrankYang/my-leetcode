class Solution {
public:
    string toLowerCase(string s) {
        std::transform(s.begin(), s.end(), s.begin(), [](char ch){
            return tolower(ch);
        });
        return s;
    }
};