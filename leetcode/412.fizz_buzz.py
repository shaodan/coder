class Solution(object):

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 1-line anwsor
        return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1,n+1)]

        if n < 1:
            return []
        result = [None]*n
        for i in xrange(n):
            num = i+1
            if num % 15 == 0:
                result[i] = 'FizzBuzz'
            elif num % 3 == 0:
                result[i] = 'Fizz'
            elif num % 5 == 0:
                result[i] = 'Buzz'
            else:
                result[i] = str(num)
        return result


s = Solution()
res = s.fizzBuzz(16)
for i,r in enumerate(res):
    print i+1, r
