# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
    # def track(self):
    #     if self.next is None:
    #         return str(self.val)+'\n'
    #     else:
    #         return str(self.val)+'->'+self.next.track()

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        prev = None
        while node is not None:
            if node.val==val:
                if prev == None:
                    node = node.next
                    del head
                    head = node
                else:
                    prev.next = node.next
                    del node
                    node = prev.next
            else:
                prev = node
                node = node.next
        return head
        
s = Solution()
l = [1, 1, 2, 3, 4, 1]
v = 1
head = ListNode(l[0])
prev = head
for i in l[1:]:
    prev.next = ListNode(i)
    prev = prev.next

print l
print v
print head.track()

head = s.removeElements(head, v)
if head is not None:
    print head.track()
else:
    print "head null"
