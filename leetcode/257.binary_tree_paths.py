# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        if not any((root.left, root.right)):
            return [str(root.val)]
        paths = self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right)
        return [str(root.val)+'->'+p for p in paths]
        
