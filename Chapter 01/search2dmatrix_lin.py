from typing import List
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        row, col = 0, len(matrix[0]) - 1
        while col >= 0 and row <= len(matrix) - 1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
''' 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        m=len(matrix)
        m0 = matrix[0]
        n = len(m0)
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == target:return True
        return False
sol=Solution()
m= [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(sol.searchMatrix(m,3))
m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(sol.searchMatrix(m,13))