#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum
#
# Medium (26.89%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
# 
# Note: The solution set must not contain duplicate quadruplets.
# 
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    """
    O(N^3) Based on 3Sum
    """
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        m = len(nums)
        for n in range(m-3):
            if n>0 and nums[n]==nums[n-1]:
                continue
            three_target = target - nums[n]
            # TIPS: margin checking
            if sum(nums[n+1:n+4]) > three_target:
                break
            if sum(nums[-3:]) < three_target:
                continue
            for i in range(n+1, m-2):
                if i>(n+1) and nums[i]==nums[i-1]:
                    continue
                tar = three_target - nums[i]
                if sum(nums[i+1:i+3]) > tar:
                    break
                if sum(nums[-2:]) < tar:
                    continue
                l, r = i+1, m-1
                while l < r:
                    two_sum = nums[l] + nums[r]
                    if  two_sum < tar:
                        l += 1
                    elif two_sum > tar:
                        r -= 1
                    else:
                        res.append([nums[n], nums[i], nums[l], nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l += 1
                        while l<r and nums[r]==nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print s.fourSum(nums, target)
