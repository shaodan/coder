# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def deleteNode(root, key):
    node = root
    leaf = None
    while not node:
        if node.val == key:
            if node.left is None:
                leaf = node.right
            elif node.right is None:
                leaf = node.left
            else:
                leaf = node.left
                while leaf.right is not None:
                    left = left.right
            node.val = leaf.val
            node.left = leaf.left
            node.right = leaf.right
            break
        elif node.val > key:
            node = node.left
        else :
            node = node.right
    return root


def travel(node):
    if node is None:
        return
    print node.val
    travel(node.left)
    travel(node.right)


null = None
# l = [0,1,2,3 ,     4 ,5,6,7          ,8,9]
l = [5,4,8,11,null,13,4,7,2,null,null,5,1]
# l =[5,3,6,2,4,null,7]
key = 3


graph = [TreeNode(x) if x is not None else None for x in l]
length = len(l)
print length
for i in xrange(length/2-1):
    if graph[i] is None:
        continue
    graph[i].left = graph[i*2+1]
    if i*2+2<=length-1:
        graph[i].right = graph[i*2+2]

# graph = map(lambda x:TreeNode(x), filter(lambda x:x is not None, l))
# graph[0].left = graph[1]
# graph[0].right = graph[2]
# graph[1].left = graph[3]
# graph[2].left = graph[4]
# graph[2].right = graph[5]
# graph[3].left = graph[6]
# graph[3].right = graph[7]
# graph[5].left = graph[8]
# graph[5].right = graph[9]

root = graph[0]
travel(root)
# deleteNode(root, key)
# travel(root)
