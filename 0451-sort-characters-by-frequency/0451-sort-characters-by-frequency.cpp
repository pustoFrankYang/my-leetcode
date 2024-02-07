class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> cnt;
        for (const char& ch : s) {
            ++cnt[ch];
        }
        
        // change map to vector to facilitate sorting
        vector<pair<char, int>> cntpairs;
        for (const auto& kv : cnt) {
            cntpairs.emplace_back(kv);
        }
        
        // sort by cnt from greater to less
        sort(cntpairs.begin(), cntpairs.end(), [](pair<char, int> a, pair<char, int> b){
            return a.second > b.second;
        });
        
        string ans = "";
        for (const auto& cntpair : cntpairs) {
            // for cntpair.second times repeat cntpair.first
            ans += string(cntpair.second, cntpair.first);
        }
        return ans;
    }
};