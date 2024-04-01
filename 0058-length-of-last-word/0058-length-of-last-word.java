class Solution {
    public int lengthOfLastWord(String s) {
        String[] t = s.strip().split(" ");
        return t[t.length - 1].length();
    }
}