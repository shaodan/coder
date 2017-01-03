#coding:utf-8
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest
#
# Medium (31.19%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
# 
# 
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
# 
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        method I: 108ms
        """
        res = None
        l = len(nums)
        res = sum(nums[:3])
        min_dis = abs(res-target)
        nums.sort()
        for i in range(l-2):
            j, k = i+1, l-1
            while j < k:
                dis = nums[i] + nums[j] + nums[k] - target
                if dis==0:
                    return target
                if abs(dis) < min_dis:
                    min_dis = abs(dis)
                    res = dis + target
                if dis > 0:
                    k -= 1
                else:
                    j += 1
        return res

    
    def threeSumClosest2(self, nums, target):
        """
        method II: 445ms
        """
        res = None
        l = len(nums)
        res = sum(nums[:3])
        min_dis = abs(res-target)
        nums.sort()
        for i in range(l-2):
            j = i+1
            k = l-1
            while j < k:
                start, end = j+1, k
                k_target = target - nums[i] - nums[j]
                while start<end:
                    k = (start+end)/2
                    if nums[k] == k_target:
                        return target
                    if nums[k] < k_target:
                        start = k+1
                    else:
                        end = k-1
                if nums[k] > k_target:
                    k = start
                if k<l-1 and abs(nums[k]-k_target) > abs(nums[k+1]-k_target):
                    k = k+1
                if  abs(nums[k]-k_target) < min_dis:
                    min_dis = abs(nums[k]-k_target)
                    res = nums[i]+nums[j]+nums[k]
                j += 1
        return res
        
if __name__=='__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    # nums = [4,-8,98,-51,73,12,-31,39,87,-16,20,69,18,59,54,44,-58,40,-36,22,-60,-8,-43,83,88,1,-25,71,-53,33,60,32,61,-5,28,38,-28,45,25,-68,-60,-87,5,-94,-19,-31,-35,-29,0,24,-62,-84,-7,-94,-89,12,97,-32,-89,92,-50,-54,-18,12,84,-81,-99,67,24,-4,-88,61,48,-17,-17,-44,65,-18,-47,68,0,-7,78,36,0,-15,23,-4,1,-74,-64,-53,-82,-10,34,-57,-93,65,-3,-73,-8,-59,96,35,51,49,92,-8,-4,-100,-64,5,-86,-26,71,60,-85,-42,-13,-10,17,-11,59,-14,-5,34,-36,24,9,78,48,24,-88,-46,-76,31,-47,-68,29,34,-97,-69,-41,-87,-42,96,0,-90,51,-55,57,86,-61,41,1,-90,-9,63,84,-32,80,-15,-12,0,72,-22,-6,-64,94,23,-80,-25,-37,-38,69,12,-64,-95,-65,5,15,-31,-68,-55,-100,-89,-24,-66,33,-14,-40,-50,-19,-79,-4]
    # target = -76
    # nums = [0,1,2]
    # target = 0
    nums = [-3,-2,-5,3,-4]
    target = -1
    r = s.threeSumClosest(nums, target)
    print r
