class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> m;
        int indL, indR, maxlen = 0;
        for (indL=0, indR=0; indR<s.size(); indR++) {
            if (m.count(s[indR])) {
                indL = max(indL, m[s[indR]]+1); // !Achtung, indL cannotMoveBack here
            }
            m[s[indR]] = indR;
            maxlen = max(maxlen, indR-indL+1);
        }
        return maxlen;
    }
};