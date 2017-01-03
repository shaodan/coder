# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        n0 = head
        head = head.next
        n0.next = head.next
        head.next = n0
        n1 = n0.next
        while n1 is not None and n1.next is not None:
            n2 = n1.next
            n0.next = n2
            n1.next = n2.next
            n2.next = n1
            n0 = n1
            n1 = n0.next
        return head


    def print2(self, head):
        if head is None:
            print "Empty List"
        else:
            while head:
                print str(head.val) + ' -> ',
                head = head.next
            print 'NULL'


if __name__ == '__main__':
    l = []
    l = [1,2,3,4]
    l = [1,2,3,4,5]
    head = ListNode(l[0]) if len(l) > 0 else None
    node = head
    for i in l[1:]:
        node.next = ListNode(i)
        node = node.next
    s = Solution()
    s.print2(head)
    head = s.swapPairs(head)
    s.print2(head)
