class Solution {
    public boolean isSubstringPresent(String s) {
        boolean[][] exists = new boolean[26][26];
        for (int i = 0; i < s.length(); i++) {
            if (i - 1 >= 0) {
                exists[s.charAt(i - 1) - 'a'][s.charAt(i) - 'a'] = true;
            }
            if (i + 1 < s.length()) {
                exists[s.charAt(i) - 'a'][s.charAt(i + 1) - 'a'] = true;
            }
        }
        for (int i = 0; i < 26; i ++) {
            for (int j = 0; j < 26; j++) {
                if (exists[i][j] && exists[j][i]) return true;
            }
        }
        return false;
    }
}