#
# [141] Linked List Cycle
#
# https://leetcode.com/graphql
#
# algorithms
# Easy (35.22%)
# Total Accepted:    217.7K
# Total Submissions: 618.1K
# Testcase Example:  '[]\nno cycle'
#
# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import structures as ss

ListNode = ss.SingleLinkedListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
        
if __name__ == '__main__':
    s = Solution()
    ls = [[],  [1], [1,2,3], [1,2,3,4]]
    for l in ls:
        print l
        ll = ListNode.from_list(l)
        
        if len(l) > 3:
            ll.next.next.next = ll
        print s.hasCycle(ll)