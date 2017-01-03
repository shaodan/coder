#
# @lc app=leetcode id=1033 lang=python3
#
# [1033] Moving Stones Until Consecutive
#
# https://leetcode.com/problems/moving-stones-until-consecutive/description/
#
# algorithms
# Easy (29.84%)
# Total Accepted:    3.3K
# Total Submissions: 10.9K
# Testcase Example:  '1\n2\n5'
#
# Three stones are on a number line at positions a, b, and c.
#
# Each turn, let's say the stones are currently at positions x, y, z with x < y
# < z.  You pick up the stone at either position x or position z, and move that
# stone to an integer position k, with x < k < z and k != y.
#
# The game ends when you cannot make any more moves, ie. the stones are in
# consecutive positions.
#
# When the game ends, what is the minimum and maximum number of moves that you
# could have made?  Return the answer as an length 2 array: answer =
# [minimum_moves, maximum_moves]
#
# Example 1:
# Input: a = 1, b = 2, c = 5
# Output: [1, 2]
# Explanation: Move stone from 5 to 4 then to 3, or we can move it directly to
# 3.
#
# Example 2:
# Input: a = 4, b = 3, c = 2
# Output: [0, 0]
# Explanation: We cannot make any moves.
#
# Note:
# 1 <= a <= 100
# 1 <= b <= 100
# 1 <= c <= 100
# a != b, b != c, c != a
#
from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        max_move = c-a-2
        # Wrong solution:
        # min_move = 1 if (b-a) > 1 else 0
        # min_move +=  1 if (c-b) > 1 else 0
        # Correct solution:
        min_move = 2 if min(b-a, c-b) > 2 else min(1, max_move)
        return [min_move, max_move]

if __name__ == '__main__':
    s = Solution()
    print(s.numMovesStones(1, 2, 5), [1, 2])
    print(s.numMovesStones(1, 4, 3), [1, 1])
    print(s.numMovesStones(3, 5, 1), [1, 2])


