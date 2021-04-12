from typing import List
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000]*(amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            mincoin=10000
            for j in range(len(coins)):
                if i - coins[j] < 0:continue
                mincoin = min(mincoin, dp[i-coins[j]]+1)
            dp[i] = mincoin
        if dp[amount] == 10000:dp[amount] = -1
        return dp[amount]
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10000]*(amount + 1)
        dp[0] = 0
        for j in coins:
            for i in range(j,amount+1):
                dp[i] = min(dp[i], dp[i-j]+1)
        return dp[amount] if dp[amount] != 10000 else -1

sol = Solution()
print(sol.coinChange([1, 2, 5],11))
