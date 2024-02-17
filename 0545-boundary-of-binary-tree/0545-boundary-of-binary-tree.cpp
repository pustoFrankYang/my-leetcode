// ！！！！！仅供复习参考用，原来写的解答的python文件自动转换的C++

#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

// Definition for a binary tree node.
// struct TreeNode {
//     int val;
//     TreeNode* left;
//     TreeNode* right;
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
// };

class Solution {
public:
    vector<int> boundaryOfBinaryTree(TreeNode* root) {
        vector<int> left, right, leafs;
        stack<pair<TreeNode*, char>> q;
        if (root->right) {
            q.push({root->right, 'r'});
        }
        if (root->left) {
            q.push({root->left, 'l'});
        }
        TreeNode* prev = nullptr;
        while (!q.empty()) {
            auto [curr, label] = q.top();
            q.pop();
            if (!curr->left && !curr->right) {
                leafs.push_back(curr->val);
                continue;
            }
            if (label == 'l') {
                left.push_back(curr->val);
                if (curr->left) {
                    if (curr->right) {
                        q.push({curr->right, 'n'});
                    }
                    q.push({curr->left, 'l'});
                } else {
                    q.push({curr->right, 'l'});
                }
            } else if (label == 'r') {
                right.push_back(curr->val);
                if (curr->right) {
                    q.push({curr->right, 'r'});
                    if (curr->left) {
                        q.push({curr->left, 'n'});
                    }
                } else {
                    q.push({curr->left, 'r'});
                }
            } else {
                if (curr->right) {
                    q.push({curr->right, 'n'});
                }
                if (curr->left) {
                    q.push({curr->left, 'n'});
                }
            }
        }
        reverse(right.begin(), right.end());
        vector<int> result;
        result.push_back(root->val);
        result.insert(result.end(), left.begin(), left.end());
        result.insert(result.end(), leafs.begin(), leafs.end());
        result.insert(result.end(), right.begin(), right.end());
        return result;
    }
};
