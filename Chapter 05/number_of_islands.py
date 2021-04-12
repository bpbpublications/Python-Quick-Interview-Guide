from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0  #Base case
        
        n_islands = 0
        nrow = len(grid)
        ncol = len(grid[0])       
        #Recursive nested function to wipe out neighbours of (row,col)
        def set_zero(row, col, grid):
            if (0 <= row <= nrow-1) and (0 <= col <= ncol-1):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    set_zero(row+1, col, grid)
                    set_zero(row-1, col, grid)
                    set_zero(row, col+1, grid)
                    set_zero(row, col-1, grid)
        #Scan the matrix for 1 value
        for row in range(nrow):
            for col in range(ncol):
                if grid[row][col] == '1':
                    n_islands += 1
                    set_zero(row, col, grid)
        
        return n_islands
#Driver code
sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print("Number of islands = ",sol.numIslands(grid))
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print("Number of islands = ",sol.numIslands(grid))