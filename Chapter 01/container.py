from typing import List  #Not needed when submitting to Leet code
class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxwater = 0 # Initialize maximum variable to 0
        l, r = 0, len(h)-1 # Define initial window of maximum size
        while l < r:
            if h[l] <= h[r]:#Find smaller height and shift its pointer inwards
                maxwater = max(maxwater, (r-l) * h[l])
                l += 1
            else:
                maxwater = max(maxwater, (r-l) * h[r])
                r -= 1
        return maxwater
nums = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(nums)
print(sol.maxArea(nums))


