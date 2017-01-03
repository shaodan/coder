#coding=utf-8
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (38.77%)
# Total Accepted:    300.7K
# Total Submissions: 775.6K
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#
ord_2 = ord("2")
table = [
    ['a', 'b', 'c'], # 2
    ['d', 'e', 'f'], # 3
    ['g', 'h', 'i'], # 4
    ['j', 'k', 'l'], # 5
    ['m', 'n', 'o'], # 6
    ['p', 'q', 'r', 's'], # 7
    ['t', 'u', 'v'], # 8
    ['w', 'x', 'y', 'z'], # 9
]

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        res = [""]
        for d in digits:
            new_res = []
            i = ord(d) - ord_2
            letters = table[i]
            for r in res:
                new_res.extend(map(lambda c: r+c, letters))
            res = new_res
        return res

if __name__ == '__main__':
    s = Solution()
    digits = ['','5', '23', '234']
    for d in digits:
        dl = list(d)
        print(d, s.letterCombinations(dl))

