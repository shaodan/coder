# coding: utf-8
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount==0:
            return 1
        l = len(coins)
        if l < 1:
            return 0
        if l==1:
            if amount%coins[0] == 0:
                return 1
            else:
                return 0
        # dp(i, j) 表示用coins的前i个coin组合成j的解的个数
        # 可以分解为：用第i个coin以及前i-1个coin组合为j；和只用前i-1个coin组合为j两种情况
        # 而前面一种情况等价于用前i个coin组合为(j-coin[i])也就是dp(i, j-coin[i])后一种为dp(i-1, j)
        # dp(i, j) = dp(i, j-coin[i]) + dp(i-1, j)
        dp = [None] * l
        rows = amount+1
        dp[0] = [0] * rows
        for j in xrange(amount/coins[0]+1):
            dp[0][j*coins[0]] = 1
        for i in xrange(1, l):
            dp[i] = [1] * rows
            last = coins[i]
            for j in xrange(1, rows):
                dp[i][j] = dp[i-1][j] + (dp[i][j-last] if j>=last else 0)
        return dp[l-1][amount]


    def change_save_space(self, amount, coins):
        dp = [ 1 if i == 0 else 0 for i in range(amount+1) ]
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]


coins = [1, 2, 5]
amount = 5

# coins = [1]
# amount = 0

# coins = [1]
# amount = 1

# coins = [5, 6, 7]
# amount = 7

# coins = [2]
# amount = 3

# coins = []
# amount = 7


s = Solution()
print s.change(amount, coins)

