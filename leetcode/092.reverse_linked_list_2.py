# coding=utf-8
import structures as ss

ListNode = ss.SingleLinkedListNode

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        1<=m<=n<=length
        """
        if not head:
            return head
        if n==m:
            return head
        if m==1:
            node = head.next
            prev = head
            cur = 2
        else:
            node = head
            cur = 2 # 从2开始计数
            while 1:
                if cur >= m:
                    break
                node = node.next
                cur += 1
            left = node
            prev = node.next
            node = prev.next
            cur += 1 # 前进两个，只加1次
        while 1:
            if cur > n:
                break
            nex = node.next
            node.next = prev
            prev = node
            node = nex
            cur += 1
        if m==1:
            head.next = node
            head = prev
        else:
            left.next.next = node
            left.next = prev
        return head





s = Solution()
ll = [1,2,3,4,5,6,7,8]
m = 2
n = 4

ll = [5]
m = 1
n = 1
head = ListNode.from_list(ll)
print head.trace()
head = s.reverseBetween(head, m, n)
print head.trace()

