"""
Test for structures.py
Author: ShaoDan(shaodan.cn@gmail.com)
"""

import pytest
from structures import ListNode, SingleLinkedListNode, DoubleLinkedListNode, LinkedList, DoubleLinkedList, Heap


class TestStructures:
    
    def test_LinkedListNode(self):
        pass
    
    def test_linked_list(self):
        def str_with_dash(l):
            return '-'.join(map(str, l))
        
        source =  [1,2,3,4,5,6]
        ll1 = LinkedList(source)
        assert list(ll1) == source
        assert str(ll1) == str_with_dash(source)
        assert len(ll1) == len(ll1)
        assert ll1.end.val == 6
        
    def test_linked_list_append(self):
        ll2 = LinkedList()
        assert str(ll2) == ''
        assert len(ll2) == 0
        assert ll2.head is None
        assert ll2.end is None
        
        ll2.append(1)
        assert list(ll2) == [1]
        ll2.append(2)
        assert list(ll2) == [1,2]
        
    def test_linked_list_extend(self):
        ex1 = [1,2,3]
        ex2 = [4,5,6]
        ex3 = []
        ll3 = LinkedList()
        ll3.extend(ex3)
        assert list(ll3) == ex3
        assert ll3.end is None
        ll3.extend(ex1)
        assert list(ll3) == ex3+ex1
        assert ll3.end.val == ex1[-1]
        ll3.extend(ex2)
        assert list(ll3) == ex3+ex1+ex2
        assert ll3.end.val == ex2[-1]
        ll3.extend(ex3)
        assert list(ll3) == ex3+ex1+ex2+ex3
        assert ll3.end.val == ex2[-1]
        
        ll4 = LinkedList()
        ll4.extend(LinkedList(ex3))
        assert list(ll4) == ex3
        assert ll4.end is None
        ll4.extend(ex1)
        assert list(ll4) == ex3+ex1
        assert ll4.end.val == ex1[-1]
        
    def test_double_linked_list(self):
        source = [1,2,3,4,5,6]
        dll = DoubleLinkedList(source)
        
        assert list(dll) == source
        assert str(dll) == '='.join(map(str, source))
        assert dll.head.val == 1
        assert dll.end.val == 6
        # assert dll.head.prev is None
        # assert dll.end.next is None
        
    
    def test_heap(self):
        pass