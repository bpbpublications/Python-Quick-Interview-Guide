from typing import List
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        for i in range(1,amount+1):
            #numways=0
            for j in range(len(coins)):
                if i - coins[j] < 0:continue
                dp[i] +=  dp[i-coins[j]]
            #dp[i] = numways
        return dp[amount]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[amount]
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(1, amount + 1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        return dp[amount]
sol = Solution()
print(sol.coinChange([1, 2, 5],5))
