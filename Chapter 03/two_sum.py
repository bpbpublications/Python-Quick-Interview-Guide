# -*- coding: utf-8 -*-
from typing import List
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
               if nums[i] + nums[j] == target:
                    return [i, j]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        htable = {}
        for i in range(len(nums)):
            if target - nums[i] in htable:
                return [htable[target - nums[i]],i]
            else:
                htable[nums[i]]=i
sol = Solution()
print(sol.twoSum([2, 7, 11, 15],9))
      
