#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/graphql
#
# algorithms
# Hard (27.82%)
# Total Accepted:    189.8K
# Total Submissions: 682K
# Testcase Example:  '[]'
#
# 
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import structures as ss
ListNode = ss.ListNode
# MinHeap = ss.MinHeap
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def iter_linked_list(self):
            node = self
            while node:
                yield node
                node = node.next
        ListNode.__iter__ = iter_linked_list
        def lt(self, other):
            return self.val < other.val
        ListNode.__lt__ = lt
        
        lists = filter(lambda n: n, lists)
        head = ListNode(1)
        node = head
        for n in heapq.merge(*lists):
            node.next = n
            node = n
        return head.next
    
    
if __name__ == '__main__':
    s = Solution()
    lists = [[1,2,4,5,13], [6,7,8,10], [9,12], [11], [3,14,15,16]]
    # lists = []
    # lists = [[]]
    # lists = [[1], []]
    # lists = [[0],[1]]
    lls = map(ss.LinkedList, lists)
    print lls
    lls = map(lambda l:l.head, lls)
    merged = s.mergeKLists(lls)
    # merged = heapq.merge(*lls)
    # print list(merged)
    ss.ListNode.print_list(merged)
