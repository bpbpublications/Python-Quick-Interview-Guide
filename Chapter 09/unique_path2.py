from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #print(obstacleGrid)
        m = len(obstacleGrid)   # Find number of columns
        n = len(obstacleGrid[0])# Find number of rows
        dp = [[0]*n for _ in range(m)]# create a 2D-matrix and initialize with  0 
        if obstacleGrid[0][0] == 1:return 0
        dp[0][0] = 1 # Number of ways of reaching top left cell = 1.
        #Initialize first column
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i-1][0] 
        #Initialize first row
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] = 0
            else:
                dp[0][j] = dp[0][j-1] 
        #Scan rest of the matrix
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        #print(dp)
sol = Solution()
print (sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))     