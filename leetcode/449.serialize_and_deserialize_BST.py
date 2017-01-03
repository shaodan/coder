# coding : utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Stack(object):
    def __init__(self, capacity=100):
        self._capacity = capacity
        self._data = [0] * self._capacity
        self._head = 0

    def pop(self):
        if self._head <= 0:
            return None
        self._head -= 1
        return self._data[self._head]

    def push(self, data):
        if self._head >= self.capacity:
            self.malloc()
        self._data[_head] = data
        self._head += 1

    def malloc(self):
        extra = (self._capacity+1)/2
        self._data = self._data + [0]*extra
        self._capacity += extra

class Codec:

    def count(self, root, null_count=0):
        if root is None :
            return null_count
        return 1 + self.count(root.left, null_count) + self.count(root.right, null_count)

    def trace(self, root):
        if root is None:
            return
        print root.val,
        self.trace(root.left)
        self.trace(root.right)

    def serialize2(self, root):
        if root is None:
            return ""
        # import math
        # depth = math.log(size(root))
        stack = Stack()
        stack.push(root)
        node = root
        while 1:
            if node.left is None:
                pass

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        size = self.count(root, 1)
        print size
        nodes = [None] * size
        nodes[0] = root
        i = 1
        j = 0
        while i < size:
            while nodes[j] is None:
                j += 1
            node = nodes[j]
            nodes[i] = node.left
            i += 1
            nodes[i] = node.right
            i += 1
            j += 1
        i = size-1
        while nodes[i] is None:
            i -= 1
        data = ','.join(['n' if n is None else str(n.val) for n in nodes[:i+1]])
        return data



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(data)==0:
            return None
        nodes = [None if x=='n' else TreeNode(int(x)) for x in data.split(',')]
        n = len(nodes)
        root = nodes[0]
        lvl_left = 0
        lvl_right = 0
        i = lvl_right+1
        while i < n:
            for j in xrange(lvl_left, lvl_right+1):
                if nodes[j] is None:
                    continue
                nodes[j].left = nodes[i]
                i += 1
                if i >= n:
                    break
                nodes[j].right = nodes[i]
                i += 1
                if i >= n:
                    break
            lvl_left = lvl_right + 1
            lvl_right = i-1
        return root


if __name__ == "__main__":

    # Your Codec object will be instantiated and called as such:
    null = 'n'
    # tree = [2,1,3, null, 0]
    tree = [5,4,8,11,null,13,4,7,2,null,null,5,1]
    nodes = map(lambda x: x if x=='n' else str(x), tree)
    data = ','.join(nodes)
    print data

    codec = Codec()
    root = codec.deserialize(data)
    codec.trace(root)
    data2 = codec.serialize(root)
    print data2
