#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays
#
# Hard (21.36%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# Example 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# 
# Example 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        imin, imax, half = 0, m, (m+n+1)/2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half - i
            if i < m and nums1[i] < nums2[j-1]:
                imin = i + 1
            elif i>0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                break
        if i==0:
            med_l = nums2[j-1]
        elif j==0:
            med_l = nums1[i-1]
        else:
            med_l = max(nums1[i-1], nums2[j-1])

        if (m+n)%2 == 1:
            return med_l
        
        if i==m:
            med_r = nums2[j]
        elif j==n:
            med_r = nums1[i]
        else:
            med_r = min(nums1[i], nums2[j])

        return (med_l + med_r) / 2.0


if __name__ == '__main__':
    #n1 = [1, 2, 5, 10]
    #n2 = [3, 4, 6, 9, 13, 14]
    n1 = [1, 3]
    n2 = [2]
    
    sol = Solution()
    print n1
    print n2
    print sol.findMedianSortedArrays(n1, n2)
