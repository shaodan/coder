#
# [70] Climbing Stairs
#
# https://leetcode.com/graphql
#
# algorithms
# Easy (40.62%)
# Total Accepted:    215.2K
# Total Submissions: 529.8K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# Input: 2
# Output:  2
# Explanation:  There are two ways to climb to the top.
# 
# 1. 1 step + 1 step
# 2. 2 steps
# 
# Example 2:
# 
# Input: 3
# Output:  3
# Explanation:  There are three ways to climb to the top.
# 
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = [1] * (n+1)
        for i in range(2,n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]
        
if __name__ == '__main__':
    s = Solution()
    params = [(1,1), (2,2), (3,3), (4,5)]
    for p1, p2 in params:
        # print p1, p2
        print s.climbStairs(p1), p2