import structures as ss

ListNode = ss.SingleLinkedListNode

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

s = Solution()
ll = [1, 2, 3, 4]
head = ListNode.from_list(ll)
print head.trace()
head = s.reverseList(head)
print head.trace()
