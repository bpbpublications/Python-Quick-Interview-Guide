from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        htable = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in htable and i - htable[num] <= k:
                return True
            htable[num] = i
        return False
    
  
    
sol=Solution()
print(sol.containsNearbyDuplicate([1,2,3,1],3))
print(sol.containsNearbyDuplicate([1,2,3,1,2,3],2))