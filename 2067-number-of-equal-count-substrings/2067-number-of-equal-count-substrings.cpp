// ¡¡¡gesah THERE ARE LIMITED POSSIBILITIES OF LEN OF THE SILDWINDOW
// 因為字母淨26總，重複都係 `count` 次，所以長度就26種可能！
// 既然可能有限，每次定len來睇即可，即容易喇
class Solution {
public:
    int equalCountSubstrings(string s, int count) {
        int n = s.size();
        int ans = 0;
        for (int time = 1; time <= 26 && time * count <= n; time ++) {
            int winlen = time * count;
            vector<int> win(26, 0);
            // count where the appearance equal to count
            // window is valid iff valider == time
            int valider = 0;
            
            // init win
            for (int i = 0; i < winlen; i ++) win[s[i] - 'a']++;
            for (int alphacnt : win) if (alphacnt == count) valider ++;
            // first window validated
            if (valider == time) ans++;
            
            // slide. q is where the right bound to become in this round
            for (int q = winlen; q < n; q ++) {
                int lefter = s[q - winlen] - 'a';
                if (win[lefter] == count) valider --;
                win[lefter] --;
                if (win[lefter] == count) valider ++;
                
                int righter = s[q] - 'a';
                if (win[righter] == count) valider --;
                win[righter] ++;
                if (win[righter] == count) valider ++;
                
                if (valider == time) ans++;
            }
        }
        
        return ans;
    }
};

// aaabbbcccddd [ ]