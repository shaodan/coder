class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if l < 3 or numRows==1 or l <= numRows:
            return s

        period = 2*(numRows-1)
        rows = [None] * numRows

        for r in xrange(numRows):
            if r == 0 or r == numRows-1:
                row = [s[i] for i in xrange(r, l, period)]
            else:
                left = [s[i] for i in xrange(r, l, period)]
                right = [s[i] for i in xrange(period-r, l, period)]
                row = [a+b for (a, b) in zip(left, right)]
                if len(left) > len(right):
                    row += left[-1]
            rows[r] = ''.join(row)

        return ''.join(rows)

    def convert_discuss(self, s, numRows):
        step = (numRows == 1) - 1  # 0 or -1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1:
                step = -step  #change direction
            idx += step
        return ''.join(rows)


sol = Solution()
s = "PAYPALISHIRING"
s = 'ABCDEFGHIJK'
# s = ''
numRows = 3
numRows = 4
# numRows = 1
print sol.convert(s, numRows)
print sol.convert_discuss(s, numRows)
