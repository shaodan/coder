#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (25.18%)
# Total Accepted:    296.8K
# Total Submissions: 1.2M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
#
# The matching should cover the entire input string (not partial).
#
# Note:
#
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
#
#
# Example 1:
#
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
#
#
# Example 2:
#
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
#
#
# Example 3:
#
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
#
#
# Example 4:
#
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
#
#
# Example 5:
#
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
#
#
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = self.parse_reg(p)
        # print r
        return self.isMatchReg(s, r)

    def isMatchReg(self, s, r):
        if len(r) == 1:
            pass
        if len(s) == 0:
            return self.match_empty(p)

        # return self.isMatchReg(s, r)

    def match_empty(self, p):
        if len(p) % 2 == 1:
            return False
        for i in range(1, len(p), 2):
            if p[i] != '*':
                return False
        return True

    def match_no_star(self, s, p):
        pass

    def isMatchReg(self, s, r):
        if len(r) == 1:
            pass

    def parse_reg(self, p):
        reg = []
        i = 1
        while i < len(p):
            if p[i] == '*':
                reg.append(p[i-1]+'*')
                i+=2
            else:
                reg.append(p[i-1])
                i+=1
        if i==len(p):
            reg.append(p[i-1])
        return reg

if __name__ == '__main__':
    sol = Solution()
    cases = [('aa', 'a'), ('aa', 'aa'), ('', 'a*b*'),("aa", "b*"),("aa", ".*"),("ab", ".*"),("aab", "c*a*b"), ("mississippi", "mis*is*p*.")]
    expects = [False, True, True, True, True, ]
    for c, e in zip(cases, expects):
        s, p = c
        print(s, p, '==>', sol.isMatch(s, p), e)
