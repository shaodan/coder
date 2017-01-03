#encoding: utf-8
# [454] 4Sum II
#
# https://leetcode.com/graphql
#
# algorithms
# Medium (47.46%)
# Total Accepted:    24.7K
# Total Submissions: 52K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
#
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is
# guaranteed to be at most 2^31 - 1.
#
# Example:
#
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# Output:
# 2
#
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#
#
#
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sum_ab = self.sum_table(A, B)
        sum_cd = self.sum_table(C, D)
        res = 0
        for k, v in sum_ab.items():
            if (-k) in sum_cd:
                res += v * sum_cd[-k]
        return res


    def sum_table(self, A, B):
        sum_table = {}
        for a in A:
            for b in B:
                t = a+b
                if t not in sum_table:
                    sum_table[t] = 1
                else:
                    sum_table[t] += 1
        return sum_table

    def fourSumCountBS(self, A, B, C, D):
        pass

if __name__ == "__main__":
    s = Solution()
    tests = [[[1,2],[-2,-1],[-1,2],[0,2]]]
    expects = [2]
    for t, e in zip(tests, expects):
        print(t, s.fourSumCount(*t), e)

