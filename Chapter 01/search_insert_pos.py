from typing import List

class Solution:#Linear search
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0: return 0
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
'''
class Solution:#Binary search
    def searchInsert(self, array: List[int], target: int) -> int:
       low = 0
       high = len(array)

       while low < high:
          middle = (high + low) // 2

          if array[middle] == target:
              return middle           #We found target

          if array[middle] < target:
             low = middle + 1         #Array is smaller than target, remove lower half

          if array[middle] > target:
             high = middle            #Array is bigger than target, remove upper half
       return low                     #Come here when low >= high
'''  
#Driver code
sol=Solution()
print(sol.searchInsert([1,3,5,6], 5))
print(sol.searchInsert([1,3,5,6], 2))
print(sol.searchInsert([1,3,5,6], 7))
print(sol.searchInsert([1,3,5,6], 0))