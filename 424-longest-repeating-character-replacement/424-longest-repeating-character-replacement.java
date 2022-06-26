class Solution {
    public int characterReplacement(String s, int k) {
        List<Integer> cnt = new ArrayList<>();
        for (int i = 0; i < 26; i ++)
            cnt.add(0);
        for (int i = 0; i < k; i ++) 
            cnt.set(s.charAt(i) - 'A', cnt.get(s.charAt(i) - 'A') + 1);
        int l = 0, r = k;
        int currmax = r - l;
        int max_freq = Collections.max(cnt);
        while (r < s.length()) {
            // move r
            cnt.set(s.charAt(r) - 'A', cnt.get(s.charAt(r) - 'A') + 1);
            max_freq = Math.max(max_freq, cnt.get(s.charAt(r) - 'A'));
            r ++;
            
            // while l is invalid, move l
            while (l < r && max_freq + k < r - l) {
                cnt.set(s.charAt(l) - 'A', cnt.get(s.charAt(l) - 'A') - 1);
                l ++;
                max_freq = Collections.max(cnt);
            }
            currmax = Math.max(currmax, r - l);
        }
        return currmax;
    }
}