// 注意，不是直线流，是可以曲线，但不能 3m->1m->2m
class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int[][] dirs = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int m = heights.length, n = heights[0].length;
        boolean[][] isPac = new boolean[m][n], isAtl = new boolean[m][n];
        Queue<int[]> pacQ = new LinkedList<>(), atlQ = new LinkedList<>();
        for (int i = 0; i < m; i ++) {
            isPac[i][0] = true;
            pacQ.offer(new int[]{i, 0});
            isAtl[i][n - 1] = true;
            atlQ.offer(new int[]{i, n - 1});
        }
        for (int i = 0; i < n; i ++) {
            isPac[0][i] = true; 
            pacQ.offer(new int[]{0, i});
            isAtl[m - 1][i] = true;
            atlQ.offer(new int[]{m - 1, i});
        }
        while (!pacQ.isEmpty()) {
            int[] curr = pacQ.poll();
            for (var dir : dirs) {
                int nx = curr[0] + dir[0], ny = curr[1] + dir[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (!isPac[nx][ny] && heights[nx][ny] >= heights[curr[0]][curr[1]]) {
                    isPac[nx][ny] = true;
                    pacQ.offer(new int[]{nx, ny});
                }
            }
        }
        while (!atlQ.isEmpty()) {
            int[] curr = atlQ.poll();
            for (var dir : dirs) {
                int nx = curr[0] + dir[0], ny = curr[1] + dir[1];
                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (!isAtl[nx][ny] && heights[nx][ny] >= heights[curr[0]][curr[1]]) {
                    isAtl[nx][ny] = true;
                    atlQ.offer(new int[]{nx, ny});
                }
            }
        }
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < m; i ++)
            for (int j = 0; j < n; j ++)
                if (isPac[i][j] && isAtl[i][j])
                    res.add(List.of(i, j));
        return res;
    }
}