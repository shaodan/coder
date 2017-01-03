#
# [14] Longest Common Prefix
#
# https://leetcode.com/graphql
#
# algorithms
# Easy (31.57%)
# Total Accepted:    232.2K
# Total Submissions: 735.5K
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        cp = strs[0]
        i = 0
        for i in range(len(cp)):
            charAtI = cp[i]
            for s in strs[1:]:
                if len(s)<=i or s[i] != charAtI:
                    return cp[:i]
        return cp[:i+1]
        


if __name__ == '__main__':
    s = Solution()
    strs = ["abc", "ab", "abd", "abcdefg"]
    cp = s.longestCommonPrefix(strs)
    print(cp)
