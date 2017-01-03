#
# [747] Min Cost Climbing Stairs
#
# https://leetcode.com/graphql
#
# algorithms
# Easy (47.14%)
# Total Accepted:    3.4K
# Total Submissions: 7.3K
# Testcase Example:  '[0,0,0,0]'
#
# 
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
# 
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
# 
# 
# Example 1:
# 
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
# 
# 
# 
# Example 2:
# 
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
# 
# 
# 
# Note:
# 
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
# 
# 
#
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        total = len(cost)
        cheap = [0] * (total+1)
        cheap[total-1] = cost[total-1]
        for i in range(total-2, -1, -1):
            cheap[i] = min(cheap[i+1], cheap[i+2]) + cost[i]
        return min(cheap[0], cheap[1])
    
    
if __name__ == '__main__':
    s = Solution()
    costs = [[0,0,0,0], [10,15,20], [1,100,1,1,1,100,1,1,100,1]]
    anses = [0, 15, 6]
    for cost, ans in zip(costs, anses):
        print s.minCostClimbingStairs(cost), ans
