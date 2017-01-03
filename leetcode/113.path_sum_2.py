# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        paths = self.pathSum2(root, sum)
        for p in paths:
            p.reverse()
        return paths
        # return map(lambda p:p.reverse(), self.pathSum2(root, sum))
        
    def pathSum2(self, node, sum):
        if node is None:
            return []
        el = sum-node.val
        if node.left is None and node.right is None:
            if el==0:
                return [[sum]]
            else:
                return []
        paths = self.pathSum2(node.left, el)+self.pathSum2(node.right, el)
        for p in paths:
            p.append(node.val)
        return paths
        # return [p.append(node.val) for p in paths]
        
