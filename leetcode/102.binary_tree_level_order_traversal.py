import imp
# from 449.serialize_and_deserialize_BST import TreeNode, Codec


fn_, path, desc = imp.find_module('449.serialize_and_deserialize_BST')
# print fn_, path, desc
mod = imp.load_module('449.serialize_and_deserialize_BST', fn_, path, desc)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        level_order = []
        level = None
        next_level = [root]
        while len(next_level) > 0:
            level = next_level
            next_level = []
            level_order.append(level)
            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

        return [[n.val for n in level] for level in level_order]

if __name__ == '__main__':

    null = 'n'
    # tree = [2,1,3, null, 0]
    # tree = [3,9,20,null,null,15,7]
    tree = [5,4,8,11,null,13,4,7,2,null,null,5,1]
    nodes = map(lambda x: x if x=='n' else str(x), tree)
    data = ','.join(nodes)

    codec = mod.Codec()
    root = codec.deserialize(data)
    # codec.trace(root)
    s = Solution()
    print s.levelOrder(root)



