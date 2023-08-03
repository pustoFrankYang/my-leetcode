class Solution {
    private:
    unordered_map<char, vector<char>> d2l = {
        {'2', {'a', 'b', 'c'}},
        {'3', {'d', 'e', 'f'}},
        {'4', {'g', 'h', 'i'}},
        {'5', {'j', 'k', 'l'}},
        {'6', {'m', 'n', 'o'}},
        {'7', {'p', 'q', 'r', 's'}},
        {'8', {'t', 'u', 'v'}},
        {'9', {'w', 'x', 'y', 'z'}},
    };
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        // 空
        if (!digits.size()) return ans;
        string curr = "";
        bt(curr, ans, digits);
        return ans;
    }
    
    void bt(string& curr, vector<string>& ans, string& digits) {
        if (curr.size() == digits.size()) {
            ans.push_back(curr);
            return;
        }
        
        for (char c : d2l[digits[curr.size()]]) {
            curr.push_back(c);
            bt(curr, ans, digits);
            curr.pop_back();
        }
    }
};