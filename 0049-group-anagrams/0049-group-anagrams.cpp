class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> dict;
        for (const string& str : strs) {
            string sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            // c++ 不需要检查是否有键，无键则创之类的步骤
            // emplace_back 更适合一点点，因为省去了拷贝开销；但因为内置类型简单所以push back 也不是不行
            dict[sorted_str].emplace_back(str);
        }
        
        vector<vector<string>> ans;
        for (const auto& kv : dict) {
            ans.emplace_back(kv.second);
        }
        return ans;
    }
};
