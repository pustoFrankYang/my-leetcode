// Q205e, runtime 14.03%, java
class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> m = new HashMap<>(), invm = new HashMap<>();
        for (int i = 0; i < s.length(); i ++) {
            if (m.containsKey(s.charAt(i))) {
                if (m.get(s.charAt(i)) != t.charAt(i)) return false;
            } else {
                if (invm.containsKey(t.charAt(i))) return false;
                m.put(s.charAt(i), t.charAt(i));
                invm.put(t.charAt(i), s.charAt(i));
            }
        }
        return true;
    }
}