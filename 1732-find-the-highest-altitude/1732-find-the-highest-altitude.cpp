class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0, curr = 0;
        for (auto d : gain) {
            curr += d;
            ans = curr > ans? curr : ans;
        }
        return ans;
    }
};