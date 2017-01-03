class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = True
        if x < 0:
            pos = False
            x = -x

        y = 0
        if x > 1000000000:
            while x > 0:
                y = y*10+(x%10)
                if y > 2147483648:
                    return 0
                x /= 10
            if pos:
                if y > 2147483647:
                    return 0
                return y
            return -y
        while x > 0:
            y = y*10+(x%10)
            x /= 10
        if pos:
            return y
        return -y

if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
    print s.reverse(0)
    print s.reverse(-123)
