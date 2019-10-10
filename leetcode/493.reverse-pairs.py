#
# [493] Reverse Pairs
#
# https://leetcode.com/graphql
#
# algorithms
# Hard (20.92%)
# Total Accepted:    9K
# Total Submissions: 43.1K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and
# nums[i] > 2*nums[j].
# 
# You need to return the number of important reverse pairs in the given array.
# 
# Example1:
# 
# Input: [1,3,2,3,1]
# Output: 2
# 
# 
# Example2:
# 
# Input: [2,4,3,5,1]
# Output: 3
# 
# 
# Note:
# 
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
# 
# 
#
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        count = 0
        for i in xrange(len(nums)):
            it = 2*nums[i]
            for j in xrange(i):
                if nums[j] > it:
                    count += 1
        return count

    def reversePairs2(self, nums):
        if len(nums) < 1:
            return 0
        n = [i*2 for i in sorted(list(set(nums)))]
        c = [0] * (len(n)+1)
        # cc = [0] * len(n)
        last = len(n)-1
        count = 0
        # print n
        for i in xrange(len(nums)):
            loc = self.binary_search(n, 2*nums[i])
            loc2 = self.binary_search(n, nums[i])
            # print "i: ", nums[i]
            # print "loc: ", loc
            # print "last: ", last
            # print "clist: ", c
            # while loc > last:
            #     c[last+1] = c[last] + n[last]
            #     last += 1
            # count += c[loc]
            count += i - sum(c[:loc+1])
            c[loc2] += 1
            # last = loc
            # print "clist: ", c
            # print "count: ", count
        return count

    def binary_search(self, n, i):
        l = 0
        r = len(n)-1
        while l<r:
            m = (l+r)/2
            if n[m] == i:
                return m
            if n[m] < i:
                l = m+1
            else:
                r = m-1
        if n[l] >= i:
            return l
        return l+1

    def reversePair_bit(self, nums):
        if len(nums) < 2:
            return 0
        count = 0
        while 1 :
            count += 1
        return count

    def reversePair_bst(self, nums):
        return 0

class BIT(object):
    def update(self, index, value):
        pass

    def search(self, index):
        pass


if __name__ == '__main__':
    nums = [1, 3, 2, 3, 1]
    nums = [2, 4, 3, 5, 1]
    s = Solution()
    print s.reversePairs(nums)

    nums = [-5,-5]
    # print s.reversePairs(nums)
    print s.reversePairs2(nums)