class Solution {
    public int maxArea(int h, int w, int[] horiCuts, int[] vertiCuts) {
        // distance against prev line
        long maxh = 0;
        Arrays.sort(horiCuts);
        for (int i = 0; i < horiCuts.length + 1; i ++) {
            long currh = 0;
            if (i == 0)
                currh = horiCuts[i] - 0;
            else if (i < horiCuts.length)
                currh = horiCuts[i] - horiCuts[i - 1];
            else
                currh = h - horiCuts[i - 1];
            maxh = maxh >= currh ? maxh : currh;
        }
        long maxw = 0;
        Arrays.sort(vertiCuts);
        for (int i = 0; i < vertiCuts.length + 1; i ++) {
            long currw = 0;
            if (i == 0)
                currw = vertiCuts[i] - 0;
            else if (i < vertiCuts.length)
                currw = vertiCuts[i] - vertiCuts[i - 1];
            else
                currw = w - vertiCuts[i - 1];
            maxw = maxw >= currw ? maxw : currw;
        }
        return (int) ((maxh * maxw) % (int)(1e9 + 7));  // 1e9 is doubl
    }
}