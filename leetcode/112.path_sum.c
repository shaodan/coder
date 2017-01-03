/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int sum) {
    int els;
    if (root == NULL) {
        return false;
    }
    els = sum - root->val;
    if (els ==0 && root->left ==NULL && root->right==NULL)
        return true;
    return hasPathSum(root->left, els) || hasPathSum(root->right, els);
}
