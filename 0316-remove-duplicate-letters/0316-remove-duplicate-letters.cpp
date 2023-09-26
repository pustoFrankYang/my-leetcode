// ¡¡¡gesah
// Greedy try add one letter per round
class Solution {
public:
    string removeDuplicateLetters(string s) {
        int n = s.size();
        if (!n) return "";

        // 遍歷啦，揾最左可加入結果嘅位置，`posToAdd`
        // 所以停住當：某字淨剩1個，或，最小字嘅最左
        int posToAdd = 0;
        int cnt[26] = { 0 };
        for (char ch : s) cnt[ch - 'a']++;
        for (int i = 0; i < n; i ++) {
            if (s[i] < s[posToAdd]) // 更新最小
                posToAdd = i;
            if (--cnt[s[i] - 'a'] == 0) // 仲要加其前嘅最小字
                break;
        }
        //string recurrer = s.substr(posToAdd);
        //recurrer.erase(remove(recurrer.begin(), recurrer.end(), s[posToAdd]), recurrer.end());
        // C++ 冇 replaceAll，試以 regex
        string recurrer = std::regex_replace(s.substr(posToAdd), std::regex(string() + s[posToAdd]), string());
        return s[posToAdd] + removeDuplicateLetters(recurrer);
    }
};