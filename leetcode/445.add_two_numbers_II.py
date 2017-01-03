# code utf-8

class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def list2link(l):
    if len(l)==0:
        return None
    head = ListNode(l[0])
    node = head
    for val in l[1:]:
        new_node = ListNode(val)
        node.next = new_node
        node = new_node
    return head


def print_trace(l):
    if l is None:
        print "LinkedList in None"
    else:
        while 1:
            print l.val,
            l = l.next
            if l is None:
                break
            print ' -> ',
        print ''


def link2list(head):
    l = []
    node = head
    while node:
        l.append(node.val)
        node = node.next
    return l


def add(l1, l2):
    l1 = link2list(l1)
    l2 = link2list(l2)

    if len(l1) < len(l2):
        lt = l1
        l1 = l2
        l2 = lt

    l2 = [0]*(len(l1)-len(l2))+l2
    carry = 0
    for i in xrange(len(l1)-1, -1,-1):
        l1[i] += l2[i]+carry
        if l1[i]>=10:
            carry = 1
            l1[i] -= 10
        else:
            carry = 0
    su = list2link(l1)
    if carry==1:
        n = ListNode(1)
        n.next = su
        su = n
    return su


l1 = []
l2 = [5,6,4]

l1 = list2link(l1)
l2 = list2link(l2)

print_trace(l1)
print '+'
print_trace(l2)
print '='
l3 = add(l1, l2)
print_trace(l3)

