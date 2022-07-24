// ¡¡¡gesah inr Iter kann move nur Lesser und nicht Greater
// Q244m, runtime 63.31%
class WordDistance {
    
    HashMap<String, ArrayList<Integer>> s2locs;

    public WordDistance(String[] wordsDict) {
        this.s2locs = new HashMap<String, ArrayList<Integer>>();
        for (int i = 0; i < wordsDict.length; i ++) {
            ArrayList<Integer> locs = this.s2locs.getOrDefault(wordsDict[i], new ArrayList<Integer>());
            locs.add(i);
            this.s2locs.put(wordsDict[i], locs);
        }
    }
    
    public int shortest(String word1, String word2) {
        ArrayList<Integer> locs1 = this.s2locs.get(word1);
        ArrayList<Integer> locs2 = this.s2locs.get(word2);
        int p = 0, q = 0;
        int minDiff = Integer.MAX_VALUE;  //
        // 当pq其一遍历完，
        // 说明最后一个位置已作为两位置之小者遍历完
        // 说明最后一个位置已和其他可能小于或大于它的位置比较过，
        // 再继续遍历另一个指针只会让它们的差更大
        while (p < locs1.size() && q < locs2.size()) {
            minDiff = Math.min(minDiff, Math.abs(locs1.get(p) - locs2.get(q)));
            // 唯增其小者 可能使 minDiff 减
            if (locs1.get(p) < locs2.get(q)) {
                p ++;
            } else {
                q ++;
            }
        }
        return minDiff;
    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(wordsDict);
 * int param_1 = obj.shortest(word1,word2);
 */