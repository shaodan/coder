#
# [745] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/graphql
#
# algorithms
# Easy (50.37%)
# Total Accepted:    4.6K
# Total Submissions: 9.2K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# 
# Given a list of sorted characters letters containing only lowercase letters,
# and given a target letter target, find the smallest element in the list that
# is larger than the given target.
# 
# Letters also wrap around.  For example, if the target is target = 'z' and
# letters = ['a', 'b'], the answer is 'a'.
# 
# 
# Examples:
# 
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
# 
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# 
# 
# 
# Note:
# 
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique
# letters.
# target is a lowercase letter.
# 
# 
#
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters)-1
        
        # trick 1
        if target >= letters[-1]:
            return letters[0]
        target = chr(ord(target)+1)
        
        while start < end:
            mid = (start+end)/2
            if letters[mid] == target:
                return target
            elif letters[mid] > target:
                end = mid
            else:
                start = mid + 1
        return letters[end]
        
        
        
if __name__ == '__main__':
    s = Solution()
    letters = ["c", "d", "d", "d", "d", "f", "f", "j"]
    params = [('a','c'),('c','d'),('d','f'),('f','j'),('g','j'),('j','c'),('k','c')]
    print letters
    for p1,p2 in params:
        print p1, p2, s.nextGreatestLetter(letters, p1)