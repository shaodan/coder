# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @staticmethod
    def fromlist(itvl):
        return [Interval(i[0], i[1]) for i in itvl]

    @staticmethod
    def tolist(itvl):
        return [(i.start, i.end) for i in itvl]

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n < 2:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        itvs = []
        itv = intervals[0]
        for i in xrange(1, n):
            prev = itv
            itv = intervals[i]
            if prev.end < itv.start:
                itvs.append(prev)
            elif prev.end < itv.end:
                itv.start = prev.start
            else:
                itv = prev
        itvs.append(itv)
        return itvs

itv = [[1,3],[2,6],[8,10],[15,18]]
itv = Interval.fromlist(itv)

s = Solution()
itv = s.merge(itv)

itv = Interval.tolist(itv)
print itv

