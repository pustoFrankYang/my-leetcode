/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// Q1457m, runtime 78.79%, Java
class Solution {
    // palin means only 0 or 1 of the cnts are odd
    private int[] cnts = new int[10];
    private int ans = 0;
    private void dfs(TreeNode node) {
        if (node.left == null && node.right == null) {
            int cntOdd = 0;
            for (int i = 1; i <= 9; i ++) {
                if (cnts[i] % 2 == 1) cntOdd ++;
                if (cntOdd >= 2) return;
            }
            ans += 1;
            return;
        }
        if (node.left != null) {
            cnts[node.left.val] ++;
            dfs(node.left);
            cnts[node.left.val] --;
        }
        if (node.right != null) {
            cnts[node.right.val] ++;
            dfs(node.right);
            cnts[node.right.val] --;
        }
    }
    public int pseudoPalindromicPaths (TreeNode root) {
        cnts[root.val] ++;
        dfs(root);
        return ans;
    }
}