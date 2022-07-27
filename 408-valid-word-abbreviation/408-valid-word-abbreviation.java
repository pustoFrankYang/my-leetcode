// Q408e, runtime
class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int p = 0, q = 0;
        while (p < word.length() && q < abbr.length()) {
            if (abbr.charAt(q) > '9') {
                if (word.charAt(p) != abbr.charAt(q))
                    return false;
                p ++;
                q ++;
            } else {
                String num = "";
                while (q < abbr.length() && abbr.charAt(q) <= '9') {
                    num += abbr.charAt(q);
                    q ++;
                }
                if (num.charAt(0) == '0') return false;
                p += Integer.parseInt(num);
                if (p > word.length()) return false;
            }
        }
        return p >= word.length() && q >= abbr.length();
    }
}
/* 
"a"
"01"
exp. false

"hi"
"hi1"
exp. false
*/