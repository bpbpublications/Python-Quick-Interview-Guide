from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        row = matrix[0]
        if len(row) == 0: return False
        #Create an array from first column of every row
        col0 = []
        for i in range(len(matrix)):col0.append(matrix[i][0])
        #print(col0)
        #Do binary search to find a eow <= target
        low =0;high=len(col0) - 1
        while low<=high:
            mid = (low+high)//2
            if col0[mid] == target:break 
            if col0[mid] < target:
                if mid == len(col0)-1:break
                if col0[mid+1] > target:break
                else:low = mid+1
            else:
                high = mid-1
        row = matrix[mid]
        print(row)
        #Now search target in row
        low =0;high=len(row) - 1
        while low<=high:
            mid = (low+high)//2
            if row[mid] == target:return True 
            if row[mid] < target:low = mid+1
            else:high = mid-1
        return False
sol=Solution()
print(sol.searchMatrix([[]],0))
#print(sol.searchMatrix([],1))
'''
m= [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
print(sol.searchMatrix(m,0))
print(sol.searchMatrix(m,10))
print(sol.searchMatrix(m,21))
'''