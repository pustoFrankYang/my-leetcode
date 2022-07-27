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
// Q114m, runtime 78.58%
// root.next = left.first
// left.last = right.first
// root.first = root
// root.last = right.last
class Solution {
    private TreeNode flatter(TreeNode root) {
        if (root == null)
            return null;
        TreeNode leftLast = flatter(root.left);
        TreeNode rightLast = flatter(root.right);
        if (leftLast != null && rightLast != null) {
            leftLast.right = root.right;
            root.right = root.left;
            root.left = null;
            return rightLast;
        } else if (leftLast == null && rightLast != null) {
            root.left = null;
            return rightLast;
        } else if (leftLast != null && rightLast == null) {
            root.right = root.left;
            root.left = null;
            return leftLast;
        } else { // both null
            root.left = null;
            return root;
        }
    } 
    public void flatten(TreeNode root) {
        TreeNode last = flatter(root);
    }
}

/*

[1,2,null,3]
exp. [1,null,2,null,3]

*/