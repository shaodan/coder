class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type b uckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets < 2:
            return 0
        buckets -= 1
        base = minutesToTest/minutesToDie + 1
        res = 0
        while buckets > 0:
            buckets /= base
            res += 1
        return res
        
