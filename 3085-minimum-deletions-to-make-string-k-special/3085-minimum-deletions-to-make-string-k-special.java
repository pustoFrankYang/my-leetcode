// After checking 'hint 3'
class Solution {
    public int minimumDeletions(String word, int k) {
        int[] cnt = new int[26];
        for (var ch : word.toCharArray()) {
            cnt[ch - 'a'] ++;
        }
        // suppose we fix this letter as lowest
        int ans = 100005;
        for (int i = 0; i < 26; i++) {
            if (cnt[i] == 0) continue;
            
            int curr = 0;
            for (int j = 0; j < 26; j++) {
                if (cnt[j] < cnt[i]) curr += cnt[j];
                else if (cnt[j] > cnt[i] + k) curr += cnt[j] - (cnt[i] + k);
            }
            
            ans = Math.min(ans, curr);
        }
        return ans;
    }
}