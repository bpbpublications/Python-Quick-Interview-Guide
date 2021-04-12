def isBadVersion(version):
   if version >= first_bad:
      return True
   return False
class Solution:
   def firstBadVersion(self, n):
      left = 1
      right = n
      while left < right:
          mid = (left+right)//2
          if isBadVersion(mid):
              right = mid
          else:
              left=mid+1
      return left
sol = Solution()
first_bad = 4
print(sol.firstBadVersion(8))


