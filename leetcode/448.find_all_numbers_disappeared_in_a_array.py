class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in nums:
            i = abs(x)-1
            if nums[i] > 0:
                nums[i] = -nums[i]
        res = []
        for i,x in enumerate(nums):
            if x > 0:
                res.append(i+1)
            else:
                nums[i] = -x
        return res
