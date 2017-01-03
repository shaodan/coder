"""
Basic Algorithms for Leetcode
"""

class Sorter(object):

    def insert_sort(self):
        pass
    
    def shell_sort(self):
        pass

    def bublle_sort(self):
        pass

    def select_sort(self):
        pass

    def quick_sort(self, array, inspace=True):
        def partion():
            pass
        pass

    def heap_sort(self, array, order='asc'):
        pass
    
    def merge_sort(self):
        pass
    

class Searcher(object):
    
    def binary_search(self, target, array, start=0, end=None):
        '''
        see also python standard library: bisect
        '''
        if len(array) == 0:
            return 0
        if end is None:
            end = len(array)-1
        last = end
        while start <= end:
            mid = (start+end)/2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid-1
            else:
                start = mid+1
        if start > last:
            return last
        if array[start] > target:
            return start
        return start+1
