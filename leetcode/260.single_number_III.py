class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        all = 0
        for n in nums:
            all ^= n
        all &= -all   # equal to all &= ~(all-1) find the last one-bit
        res = [0, 0]
        for n in nums:
            if (all&n):
                res[0]^= n
            else:
                res[1]^=n
        return res
