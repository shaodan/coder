#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer
#
# Easy (46.11%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
#
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        last = mapping[s[0]]
        if len(s) < 2:
            return last
        for r in s[1:]:
            cur = mapping[r]
            if last < cur:
                res -= last
            else:
                res += last
            last = cur
        res += cur
        return res
        
        
if __name__ == '__main__':
    s = Solution()
    st = 'DCXXI'
    r = s.romanToInt(st)
    print(r)
        
