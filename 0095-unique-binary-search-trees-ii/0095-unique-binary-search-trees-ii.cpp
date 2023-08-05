/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
// !!所有可能的左子树可以和所有可能的右子树结合。故独立算再结合可矣。
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        return btTrees(1, n);
    }
    vector<TreeNode*> btTrees(int from, int to) {
        vector<TreeNode*> ans;
        if (from > to)
            return vector<TreeNode*>({NULL});
        if (from == to)
            return vector<TreeNode*>({new TreeNode(from)});

        for (int i = from; i <= to; i ++) {
            vector<TreeNode*> ltrees = btTrees(from, i - 1);
            vector<TreeNode*> rtrees = btTrees(i + 1, to);
            
            for (auto l : ltrees)
                for (auto r : rtrees) {
                    TreeNode* ntree = new TreeNode(i, l, r);
                    ans.push_back(ntree);
                }
        }
        
        return ans;
    }
    
};