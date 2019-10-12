/*
 * @lc app=leetcode id=938 lang=c
 *
 * [938] Range Sum of BST
 *
 * https://leetcode.com/problems/range-sum-of-bst/description/
 *
 * algorithms
 * Easy (78.09%)
 * Total Accepted:    105.6K
 * Total Submissions: 135.3K
 * Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
 *
 * Given the root node of a binary search tree, return the sum of values of all
 * nodes with value between L and R (inclusive).
 *
 * The binary search tree is guaranteed to have unique values.
 *
 * Example 1:
 *
 * Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
 * Output: 32
 *
 * Example 2:
 *
 * Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
 * Output: 23
 *
 * Note:
 *
 * The number of nodes in the tree is at most 10000.
 * The final answer is guaranteed to be less than 2^31.
 *
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int rangeSumBST(struct TreeNode* root, int L, int R){
    if (root == NULL) {
        return 0;
    }
    int sum = root->val <= R && root->val >=L ? root->val : 0;
    if (root->val < R) {
        sum += rangeSumBST(root->right, L, R);
    }
    if (root->val > L) {
        sum += rangeSumBST(root->left, L, R);
    }
    return sum;
}

