// Q937m, runtime, java
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letlogs = new ArrayList<>(), diglogs = new ArrayList<>();
        for (var log : logs) {
            String[] words = log.split(" ");  // gr
            boolean isLet = false;
            for (int i = 1; i < words.length && !isLet; i ++) {
                for (var ch : words[i].toCharArray()) {  // gr
                    if (ch >= 'a' && ch <= 'z') {
                        isLet = true;
                        letlogs.add(log);
                        break;
                    }
                }
            }
            if (!isLet)
                diglogs.add(log);
        }
        letlogs.sort((a, b) -> { // gr
            int a0 = 0, b0 = 0;
            while (a.charAt(a0) != ' ') a0 ++;
            while (b.charAt(b0) != ' ') b0 ++;
            int p = a0, q = b0;
            while (p < a.length() && q < b.length() && a.charAt(p) == b.charAt(q)) {p++; q++;}
            if (p < a.length() && q == b.length()) return 1;
            else if (p == a.length() && q < b.length()) return -1;
            else if (p < a.length() && q < b.length()) return a.charAt(p) - b.charAt(q);
            else {
                int i = 0, j = 0;
                while (a.charAt(i) == b.charAt(j)) {i++; j++;}
                return a.charAt(i) - b.charAt(j);
            }
        });
        // gr
        return Stream.concat(letlogs.stream(), diglogs.stream()).toArray(String[]::new);
    }
}