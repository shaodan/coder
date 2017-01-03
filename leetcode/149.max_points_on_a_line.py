# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        size = len(points)
        if size < 2:
            return size
        m = 1
        i = 1
        while i < size:
            k = [None]*size
            a = points[i-1]
            same = 1
            m_dict = {}
            j = i
            while j < size:
                b = points[j]
                if a.x != b.x:
                    k[j] = float(a.y-b.y)/(a.x-b.x)
                elif a.y == b.y:
                    size -= 1
                    same += 1
                    points[j] = points[size]
                    continue
                else:
                    k[j] == 'inf'
                j += 1
            while j > i:
                k_j = k[j-1]
                if k_j not in m_dict:
                    m_dict[k_j] = 0
                m_dict[k_j] += 1
                j -= 1
            if len(m_dict)>0:
                m_i = max(m_dict.values()) + same
            else:
                m_i = same
            if m_i > m:
                m = m_i
            if m >= size-i+1:
                break
            i += 1
        return m
