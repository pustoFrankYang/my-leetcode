// Q1762m, runtime 99.90%
class Solution {
    public int[] findBuildings(int[] heights) {
        int currmax = 0;
        List<Integer> res = new ArrayList<>();
        for (int i = heights.length - 1; i >= 0; i --) {
            if (heights[i] > currmax) {
                res.add(i);
            }
            currmax = currmax >= heights[i] ? currmax : heights[i];
        }
        Collections.reverse(res);
        return res.stream().mapToInt(i -> i).toArray();
    }
}