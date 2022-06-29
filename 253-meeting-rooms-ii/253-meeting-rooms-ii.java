class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        int[] begins = new int[n];
        int[] ends = new int[n];
        for (int i = 0; i < n; i ++) {
            begins[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        // ¡sort bitte
        Arrays.sort(begins);
        Arrays.sort(ends);
        int i = 0, j = 0, cnt = 0, maxcnt = 0;
        while (i < n && j < n) {
            if (begins[i] < ends[j]) {
                // the scan line meets a begin pnt
                cnt ++;
                i ++;
            } else {
                // if equal, should first reduce,
                // cuz [a,b] [b,c] can use one room
                cnt --;
                j ++;
            }
            maxcnt = Math.max(maxcnt, cnt);
        }
        return maxcnt;
    }
}