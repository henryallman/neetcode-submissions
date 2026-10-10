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

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) return 0;
        int max_diameter = 0;
        helper(root, max_diameter);
        return max_diameter;
    }

    int helper(TreeNode * node, int& max_diameter) {
        if (node == nullptr) return 0;
        int left = helper(node->left, max_diameter);
        int right = helper(node->right, max_diameter);
        max_diameter = max(max_diameter, left + right);
        return 1 + max(left, right);
    }
};
