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
// Q366m, runtime 100.00%
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        this.ord2nod = new HashMap<Integer, List<Integer>>();
        int rootOrder = rec(root);
        List<List<Integer>> ans = new ArrayList<>(); // !!!init can empty templ
        for (int i = 1; i <= rootOrder; i ++) {
            ans.add(this.ord2nod.get(i));
        }
        return ans;
    }
    private HashMap<Integer, List<Integer>> ord2nod;
    private int rec(TreeNode root) {
        if (root == null) return 0;
        int lOrd = rec(root.left);
        int rOrd = rec(root.right);
        int rootOrder = Math.max(lOrd, rOrd) + 1;
        if (this.ord2nod.get(rootOrder) == null)
            this.ord2nod.put(rootOrder, new ArrayList<Integer>());
        ord2nod.get(rootOrder).add(root.val);
        return rootOrder;
    }
}