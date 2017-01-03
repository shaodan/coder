import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        root = int(math.sqrt(n))
        self.root = [x*x for x in range(1, root+1)]
        self.num = [0] * (n+1)

        # dynamic programming
        for i in xrange(1, n+1):
            self.num[i] = min([self.num[i-x*x] for x in xrange(1, int(math.sqrt(i))+1)])+1
        return self.num[n]

    def is_square(self, n):
        sqrt_n = int(math.sqrt(n))
        return (sqrt_n*sqrt_n == n)

    # Based on Lagrange's Four Square theorem, there
    # are only 4 possible results: 1, 2, 3, 4.
    def numSquares_math(self, n):
        # If n is a perfect square, return 1.
        if self.is_square(n):
            return 1

        # The result is 4 if and only if n can be written in the
        # form of 4^k*(8*m + 7). Please refer to Legendre's three-square theorem.
        while ((n & 3) == 0): # n%4 == 0
            n >>= 2
        if ((n & 7) == 7): # n%8 == 7
            return 4

        # Check whether 2 is the result.
        sqrt_n = int(math.sqrt(n));
        for i in xrange(1, sqrt_n+1):
            if (self.is_square(n - i*i)):
                return 2
        return 3;

s = Solution()
n = 19999
# print s.numSquares(n)
print s.numSquares_math(n)
