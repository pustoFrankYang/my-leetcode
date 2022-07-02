class Solution {
    public int[] findBuildings(int[] heights) {
        int currmax = 0, nextind = 0;
        int[] res = new int[heights.length];
        for (int i = heights.length - 1; i >= 0; i --) {
            if (heights[i] > currmax) {
                res[nextind] = i;
                nextind ++;
            }
            currmax = currmax >= heights[i] ? currmax : heights[i];
        }
        int[] ans = new int[nextind];
        for (int i = nextind - 1; i >= 0; i --)
            ans[nextind - i - 1] = res[i];
        return ans;
    }
}