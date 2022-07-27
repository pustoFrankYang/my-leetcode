// Q408e, runtime 10.37%
class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        int p = 0, q = 0;
        int wordLen = word.length(), abbrLen = abbr.length();
        while (p < wordLen && q < abbrLen) {
            if (abbr.charAt(q) > '9') {
                if (word.charAt(p) != abbr.charAt(q))
                    return false;
                p ++;
                q ++;
            } else {
                String num = "";
                while (q < abbrLen && abbr.charAt(q) <= '9') {
                    num += abbr.charAt(q);
                    q ++;
                }
                if (num.charAt(0) == '0') return false;
                p += Integer.parseInt(num);
                if (p > wordLen) return false;
            }
        }
        return p >= wordLen && q >= abbrLen;
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