// Q38m, runtime 13.44%, java
class Solution {
    public String countAndSay(int n) {
        String s = "1";
        for (int i = 0; i < n - 1; i ++) {
            s = say(s);
        }
        return s;
    }
    private String say(String s) {
        String ans = "";
        char curr = s.charAt(0);
        int cnt = 1;
        if (s.length() == 1) return "1" + s;
        for (int i = 1; i < s.length(); i ++) {
            if (s.charAt(i) == curr) {
                cnt ++;
            } else {
                ans += Integer.toString(cnt) + curr;
                curr = s.charAt(i);
                cnt = 1;
            }
        }
        ans += Integer.toString(cnt) + curr;
        return ans;
    }
}