#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring
#
# Medium (25.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example:
# 
# Input: "babad"
# 
# Output: "bab"
# 
# Note: "aba" is also a valid answer.
# 
# 
# 
# Example:
# 
# Input: "cbbd"
# 
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ''
        
        i = 0
        m = 1
        start = 0
        last = len(s) - 1
        while i < last:
            j = i
            while j < last and s[j+1] == s[j]:
                j += 1
            k, l = self.is_palindromic(s, i, j)
            if l > m:
                m = l
                start = k
                # print m, s[start:start+m]
            i = j + 1
        return s[start:start+m]

    def is_palindromic(self, s, l, r):
        i = 0
        for i in range(1, min(l+1, len(s)-r)):
            if s[l-i] != s[r+i]:
                i -= 1
                break
        k = l-i
        return k, r+i-k+1


if __name__ == '__main__':
    sl = Solution()
    s = 'babad'
    s = 'abcdefg'
    s = 'abaaba'
    s = 'aaaaaaa'
    s = 'aaaaaaaaacacaaaaaa'
    print sl.longestPalindrome(s)

