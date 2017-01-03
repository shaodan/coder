class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # cheating
        # return [0, 9, 987, 123, 597, 677, 1218, 877, 475][n]
        if n == 1:
            return 9
        prd = 0
        # max_i = self.get_max()[n]
        max_i = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999][n-1]
        # min_i = max_i / 10
        # for i in xrange(max_i, min_i, -1):
        #     for j in xrange(i, min_i, -1):
        #         prd = i * j
        #         if self.isPalindrome(prd):
        #             print prd
        #             return int(prd % 1337)
        for left in xrange(max_i-1, max_i/10, -1):
            prd = self.palindromefy(left)
            i = max_i
            while i*i >= prd:
                if prd % i == 0:
                    return int(prd % 1337)
                    # return i, prd
                i -= 1
        return 0

    def palindromefy(self, left):
        right = 0
        num = left
        while left > 0:
            right = (right*10)+(left % 10)
            num *= 10
            left //= 10
        return right + num

    def isPalindrome(self, n):
        digit = [0] * (2*n)
        num = 0
        while n > 0:
            digit[num] = n % 10
            num += 1
            n = n / 10
        last = num-1
        for i in xrange(num/2):
            if digit[i] != digit[last-i]:
                return False
        return True

    def get_max(self, n):
        max_i = [0] * n
        max_ = 0
        for i in xrange(1, n+1):
            max_ = max_ * 10 + 9
            max_i[i-1] = max_
        return max_i


s = Solution()
for i in xrange(1,9):
    print "%d: %d" % (i, s.largestPalindrome(i))
# print s.largestPalindrome(3)
# print s.isPalindrome(9109)
# print s.palindromefy(101)
