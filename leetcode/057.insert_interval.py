#   coding : utf-8

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def insertInterval(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    l = len(intervals)
    if l == 0:
        return [newInterval]

    i1, l1 = search(intervals, newInterval.start)
    if i1==l:
        return intervals + [newInterval]
    i2, l2 = search(intervals, newInterval.end, start=i1)

    start = intervals[i1].start if l1==0 else newInterval.start
    end = intervals[i2].end if l2==0 else newInterval.end
    itv = Interval(start, end)
    return intervals[:i1] + [itv] + intervals[i2+1+l2:]

def search(intervals, target, start=None):
    """
    :type intervals: List[Interval]
    :type target: target
    :rtype index: int
    :rtype loc: -1 left-out;0 in;1
    """
    if start is None or start < 0:
        start = 0
    end = len(intervals)-1
    while end>start:
        mid = (start+end)/2
        itv = intervals[mid]
        if target > itv.end:
            start = mid+1
        elif target < itv.start:
            end = mid-1
        else:
            return mid, 0
    itv = intervals[start]
    if target > itv.end:
        return start+1, -1
    if target < itv.start:
        return start, -1
    return start, 0



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
intervals = [[1, 5]]
newInterval = [17, 20]
newInterval = [6, 8]
intervals = [Interval(pair[0], pair[1])  for pair in intervals]
newInterval = Interval(newInterval[0], newInterval[1])
# for i in xrange(18):
#     print i, search(intervals, i)
res = insertInterval(intervals, newInterval)
print [(itv.start, itv.end) for itv in res]
