class Solution {
public:
    string frequencySort(string s) {
        // use vector of ASCII length to avoid hashmap
        vector<pair<char, int>> cntpairs(128);
        for (const char& ch : s) {
            cntpairs[int(ch)].first = ch;
            ++cntpairs[int(ch)].second;
        }
        
        // change map to vector to facilitate sorting
        // vector<pair<char, int>> cntpairs;
        // for (const auto& kv : cnt) {
        //     cntpairs.emplace_back(kv);
        // }
        
        // sort by cnt from greater to less
        sort(cntpairs.begin(), cntpairs.end(), [](pair<char, int> a, pair<char, int> b){
            return a.second > b.second;
        });
        
        stringstream ans;
        for (const auto& cntpair : cntpairs) {
            // for cntpair.second times repeat cntpair.first
            ans << string(cntpair.second, cntpair.first);
        }
        return ans.str();
    }
};