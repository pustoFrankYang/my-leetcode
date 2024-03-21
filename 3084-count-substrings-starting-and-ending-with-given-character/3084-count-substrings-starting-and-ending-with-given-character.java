class Solution {
    public long countSubstrings(String s, char c) {
        long cnt = 0;
        for (var ch : s.toCharArray()) {
            if (ch == c) cnt++;
        }
        return (cnt) * (cnt + 1) / 2;
    }
}