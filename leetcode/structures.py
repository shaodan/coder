"""
Basic Data Structures for Leetcode
Author: ShaoDan(shaodan.cn@gmail.com)
"""

class Structure(object):
    pass
#     def __str__():
#         pass

#     def __iter__(self):
#         pass


class Node(object):
    def __init__(self, v):
        self.val = v

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return '{}({!s})'.format(self.__class__.__name__, self.val)

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val


class ListNode(Node):
    def __init__(self, v):
        self.val = v
        self.next = None

    def link(self, n):
        self.next = n
        return n

    def rlink(self, p):
        p.next = self
        return p

    @classmethod
    def from_list(cls, l):
        return LinkedList(l).head

    @staticmethod
    def print_list(head):
        print(LinkedList(head))

    def trace(self, max_length=1000):
        node = self
        node_list = []
        length = 0
        while node:
            if length > max_length:
                raise Exception('list is too long!')
            node_list.append(str(node.val))
            node = node.next
            length += 1
        # print '->'.join(node_list)
        return node_list

SingleLinkedListNode = ListNode


class DoubleLinkedListNode(ListNode):
    def __init__(self, v):
        self.val = v
        self.next = None
        self.prev = None

    def link(self, n):
        self.next = n
        n.prev = self
        return n

    def rlink(self, p):
        self.next = p
        if p:
            p.prev = self
        return p

    @classmethod
    def from_list(cls, l):
        return DoubleLinkedList(l).head
        if l is None:
            return None
        assert(isinstance(l, list))
        if len(l) < 1:
            return None
        head = ListNode(l[0])
        prev = head
        for i in l[1:]:
            node = ListNode(i)
            prev.next = node
            node.prev = prev
            prev = node
        return head


class LinkedList(Structure):
    NodeClass = ListNode
    def __init__(self, iterable=None):
        """
        :param iterable: list-like values
        """
        if iterable is None:
            self.head = None
            self.end = None
        else:
            hat = self.NodeClass(None)
            cur = hat
            for n in iterable:
                node = self.NodeClass(n)
                cur = cur.link(node)
            self.head = hat.next
            self.end = cur
            del hat

    def append(self, n):
        """
        :param n: new value add to list
        """
        node = self.NodeClass(n)
        if not self.end:
            self.head = node
        else:
            self.end.link(node)
        self.end = node

    def extend(self, iterable):
        """
        :param iterable: LinkedList or list-like values
        """
        if not self.head:
            hat = self.NodeClass(None)
            self.end = hat

        if isinstance(iterable, self.__class__):
            if iterable.head:
                self.end.link(iterable.head)
                self.end = iterable.end
        else:
            cur = self.end
            for n in iterable:
                node = self.NodeClass(n)
                cur = cur.link(node)
            self.end = cur

        if not self.head:
            self.head = hat.next
            if not self.head:
                self.end = None
            del hat

    def reloc(self, head):
        self.head = head

    def reverse(self):
        cur = self.head
        prev = None
        while cur:
            cur.link(prev)
            n = cur.next
            cur.next = prev
            # dll
            prev.prev = cur
            # end dll
            prev = cur
            cur = cur.next
        if prev:
            self.head = prev

    def __len__(self):
        c = 0
        cur = self.head
        while cur:
            c += 1
            cur = cur.next
        return c

    def __iter__(self):
        for node in self.node_iter():
            yield node.val

    def node_iter(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        return '-'.join(map(str, self))

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, str(self))


class DoubleLinkedList(LinkedList):
    NodeClass = DoubleLinkedListNode
    def reverse(self):
        pass

    def __str__(self):
        return '='.join(map(str, self))


class TreeNode(Node):
    def __init__(self, v):
        self.val = v


class BinaryTreeNode(TreeNode):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def size(self):
        return 1 + self.left.size() if self.left else 0 + self.right.size() if self.right else 0

    def depth(self):
        return max(1, self.left.depth() if self.left else 0, self.right.depth() if self.right else 0)

    def trace(self, depth):
        print root.val
        self.trace(root.left)
        self.trace(root.right)


class BinaryIndexTreeNode(BinaryTreeNode):
    def __init__(self, val):
        self.val = val


class BinarySearchTreeNode(BinaryTreeNode):
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


class Heap(Structure):
    def __init__(self, size, mim_heap=True):
        self.size = size
        self.data = [None] * size
        self.current_size = 0

    def build(self, data):
        self.size = len(data)

    def pop(self):
        if self.current_size == 0:
            return None
        self.current_size -= 1
        return self.data[0]

    def push(self):
        self.current_size = 1
