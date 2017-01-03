/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        return dfs(root, 1);
    }
    
    int dfs(TreeNode* node, int depth) {
        if (node == NULL)
            return depth-1;
        int left = dfs(node->left, depth+1);
        int right = dfs(node->right, depth+1);
        return left>right ? left : right;
    }
};
