class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        string sorted_str = "";
        unordered_map<string, vector<string>> dict;
        for (const string& str : strs) {
            sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            if (!dict.count(sorted_str)) {
                // 记得这里的新建vec不能用new哦
                dict[sorted_str] = vector<string>();
            }
            dict[sorted_str].push_back(str);
        }
        
        vector<vector<string>> ans;
        for (const auto& kv : dict) {
            ans.push_back(kv.second);
        }
        return ans;
    }
};