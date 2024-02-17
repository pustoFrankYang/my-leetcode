

// ！！！！只是把原来写的代码自动转cpp来观察


#include <vector>
#include <unordered_map>

using namespace std;

// Definition for a binary tree node.
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
// };

class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        vector<int> pathToRoot, result;
        unordered_map<TreeNode*, TreeNode*> parent; // 用于记录每个节点的父节点

        // Step 1: 从根节点到目标节点的路径
        findPathToRoot(root, target, parent, pathToRoot);

        // Step 2: 从目标节点开始DFS遍历，找到距离目标节点为k的节点
        dfs(target, nullptr, 0, k, result, parent);

        return result;
    }

private:
    unordered_map<TreeNode*, TreeNode*> parent; // 记录每个节点的父节点

    // 辅助函数：找到从根节点到目标节点的路径，并记录每个节点的父节点
    void findPathToRoot(TreeNode* node, TreeNode* target, unordered_map<TreeNode*, TreeNode*>& parent, vector<int>& pathToRoot) {
        if (!node) return;
        if (node == target) {
            getPath(node, pathToRoot);
            return;
        }
        if (node->left) {
            parent[node->left] = node;
            findPathToRoot(node->left, target, parent, pathToRoot);
        }
        if (node->right) {
            parent[node->right] = node;
            findPathToRoot(node->right, target, parent, pathToRoot);
        }
    }

    // 辅助函数：从当前节点回溯到根节点，记录路径上的节点值
    void getPath(TreeNode* node, vector<int>& pathToRoot) {
        while (node) {
            pathToRoot.push_back(node->val);
            node = parent[node];
        }
    }

    // 辅助函数：DFS遍历二叉树，找到距离目标节点为k的节点
    void dfs(TreeNode* node, TreeNode* from, int depth, int k, vector<int>& result, unordered_map<TreeNode*, TreeNode*>& parent) {
        if (!node) return;
        if (depth == k) {
            result.push_back(node->val);
            return;
        }
        if (node->left != from) {
            dfs(node->left, node, depth + 1, k, result, parent);
        }
        if (node->right != from) {
            dfs(node->right, node, depth + 1, k, result, parent);
        }
        if (parent[node] != from) {
            dfs(parent[node], node, depth + 1, k, result, parent);
        }
    }
};
