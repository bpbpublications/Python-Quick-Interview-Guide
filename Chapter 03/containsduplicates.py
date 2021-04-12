'''
class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    if nums[i] == nums[j]:
                        return True
        return False
  
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:return True
        return False    
   
class Solution:
    def containsDuplicate(self, nums):    
        return True if len(set(nums)) < len(nums) else False
'''       
class Solution:
    def containsDuplicate(self, nums):       
        htable = {}
        for n in nums:
            if n in htable: return True
            else: htable[n] = 1
        return False
    
  
    
sol=Solution()
print(sol.containsDuplicate([1,2,3,4]))
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))