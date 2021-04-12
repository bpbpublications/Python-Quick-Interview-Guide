from typing import List 
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        strt = end = -1
        for i in range(len(nums)):
            if nums[i] == target: 
                strt = i
                break
        if strt == -1:
            return [-1,-1]
        #We came here because start was found    
        for i in range(strt, len(nums)):
            if nums[i] != target:
                end = i-1
                break
            end = len(nums)-1
        return [strt,end]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return[self.getLeft(nums,target),self.getRight(nums,target)]

    def getLeft(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid-1 >= 0 and nums[mid-1] != target or mid == 0):
                    return mid
                right = mid-1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid+1

        return -1

    def getRight(self, nums, target):
        left = 0
        right = len(nums)-1

        while(left <= right):
            mid = left+(right-left)//2
            if(nums[mid] == target):
                if(mid+1 < len(nums) and nums[mid+1] != target or mid == len(nums)-1):
                    return mid
                left = mid+1
            elif(nums[mid] > target):
                right = mid-1
            else:
                left = mid+1

        return -1

sol = Solution()
nums=[5,7,7,9,9,8]
target =7
print(sol.searchRange(nums,target))
