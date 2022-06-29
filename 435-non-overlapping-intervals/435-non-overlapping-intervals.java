// ¡¡¡ gesah
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        // sort accrd. end point
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));
        
        int currend = intervals[0][1];
        int cnt = -1;  // the first one repeated
        for (var i : intervals) {
            if (i[0] >= currend) {  // update to cmp new one
                currend = i[1];
            } else {
                cnt ++;
            }
        }
        return cnt;
    }
}