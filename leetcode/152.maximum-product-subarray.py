#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/
#
# algorithms
# Medium (26.33%)
# Total Accepted:    123K
# Total Submissions: 467K
# Testcase Example:  '[-2]'
#
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
#
#
# Example 1
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        res, cmax_pos, cmax_neg = 0, 1, 1
        for i in nums:
            if i == 0:
                cmax_neg, cmax_pos = 1, 1
            elif cmax_neg > 0:
                if i > 0:
                    cmax_pos *= i
                    res = max(res, cmax_pos)
                else:
                    cmax_neg = i * cmax_pos
                    cmax_pos = 1
            else:
                if i > 0:
                    cmax_pos *= i
                    cmax_neg *= i
                    res = max(res, cmax_pos)
                else:
                    cmax_pos, cmax_neg = cmax_neg * i, cmax_pos * i
                    res = max(res, cmax_pos)
        return res


if __name__ == '__main__':
    s = Solution()
    tests = [[-2], [2,3,-2,4], [-2,0,-1], [2, 3, -2, 0, 4, -1, -2]]
    expects = [-2, 6, 0, 1]
    for t, e in zip(tests, expects):
        print(t, s.maxProduct(t), e)
