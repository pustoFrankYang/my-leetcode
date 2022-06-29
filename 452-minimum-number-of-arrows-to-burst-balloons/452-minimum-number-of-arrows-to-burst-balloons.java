class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[1]));
        
        int currend = points[0][1];
        int cnt = 1;
        for (var p : points) {
            if (p[0] > currend) {
                currend = p[1];
                cnt ++;
            }
        }
        return cnt;
    }
}