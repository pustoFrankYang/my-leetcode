/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
// Q1457m, runtime 100.00%, JS
var cnts = [];
var ans = 0;
const dfs = (node) => {
    if (node.left == undefined && node.right == undefined) {
        let cntOdd = 0;
        for (var i = 1; i <= 9; i ++) {
            if (cnts[i] % 2 == 1) cntOdd ++;
            if (cntOdd >= 2) return;
        }
        ans ++;
        return;
    }
    if (node.left != undefined) {
        cnts[node.left.val] ++;
        dfs(node.left);
        cnts[node.left.val] --;
    }
     if (node.right != undefined) {
        cnts[node.right.val] ++;
        dfs(node.right);
        cnts[node.right.val] --;
    }
}
var pseudoPalindromicPaths  = function(root) {
    ans = 0;
    for (var i = 0; i <= 9; i ++) {
        cnts[i] = 0;
    }
    cnts[root.val] ++;
    dfs(root);
    return ans;
};