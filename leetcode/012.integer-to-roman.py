#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman
#
# Medium (45.07%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# Given an integer, convert it to a roman numeral.
# 
# 
# Input is guaranteed to be within the range from 1 to 3999.
#
class Solution(object):
    
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        i = 0
        while num > 0:
            a = num / 10
            r = num - a*10
            num = a
            if r < 4:
                res = order[i]*r + res
            elif r == 4:
                res = order[i]+order[i+1] + res
            elif r < 9:
                res = order[i+1]+order[i]*(r-5) + res
            else:
                res = order[i]+order[i+2] + res
            i += 2

        return res
    
if __name__ == '__main__':
    s = Solution()
    test = [1, 4, 9, 10, 13, 620, 699, 3998, 3999]
    for t in test:
        print t, s.intToRoman(t)
    
        
