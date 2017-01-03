class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = amount+1
        res = [0]*MAX
        for i in xrange(1, MAX):
            min_r = MAX
            for j in coins:
                if i>=j and min_r > res[i-j]+1:
                    min_r = res[i-j]+1
            res[i] = min_r
        if res[amount]==MAX:
            return -1
        return res[amount]


s = Solution()
coins = [1,2,5]
amount = 11
#coins = [2]
#amount = 11
print s.coinChange(coins, amount)
