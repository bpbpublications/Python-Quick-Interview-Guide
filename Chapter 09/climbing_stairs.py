'''
class Solution:
    def  climbStairs(self, n: int) -> int:
        if (n == 1):
            return 1;
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1) :
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n <= 3:
            return n
        f_n1 = 2
        f_n2 = 1
        for i in range(3,n+1):
            f = f_n1 + f_n2
            f_n2 = f_n1
            f_n1 = f
        return f 
    
sol = Solution()
for j in range(6):
    print(j,sol.climbStairs(j))
 