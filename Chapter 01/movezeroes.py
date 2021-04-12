from typing import List  #Not needed when submitting to Leet code
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        e=0
        s=0
        for e in range(0,len(nums)): # shift non zero elements
            if nums[e]:
                nums[s] = nums[e]
                s += 1
                e += 1
            else:
                e+=1
        while s < len(nums): # fill remaining array with zeroes.
            nums[s]=0
            s += 1
nums = [0,1,0,3,12]
sol = Solution()
print(nums)
sol.moveZeroes(nums)
print(nums)

      
  