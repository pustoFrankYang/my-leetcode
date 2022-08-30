// Q48m, runtime 100%
class Solution {
    public void rotate(int[][] m) {
        int n = m.length;
        int ilimit = (n + 1) / 2, jlimit = n / 2;
        for (int i = 0; i < ilimit; i++) {
            for (int j = 0; j < jlimit; j++) {
                int t = m[i][j];
                m[i][j] = m[n - 1 - j][i];
                m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j];
                m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i];
                m[j][n - 1 - i] = t;
            }
        }
    }
}