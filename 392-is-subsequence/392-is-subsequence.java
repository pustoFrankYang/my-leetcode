// Q392e, runtime 91.85%, java
class Solution {
    public boolean isSubsequence(String s, String t) {
        int p = 0, q = 0;
        while (p < s.length() && q < t.length()) {
            while (q < t.length() && s.charAt(p) != t.charAt(q))
                q ++;
            if (q < t.length() && s.charAt(p) == t.charAt(q)) {
                p ++;
                q ++;
            }
        }
        if (p < s.length()) return false;
        return true;
    }
}