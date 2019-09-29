#class Solution:
#  def singleNumber(self,nums):
#    noDuplicates = []
#    for i in nums:
#      if i not in noDuplicates:
#        noDuplicates.append(i)
#      else:
#        noDuplicates.remove(i)
#    return noDuplicates.pop()
#O(n) time
#O(n) space

class Solution:
  def singleNumber(self,nums):
    xor = 0
    for i in nums:
        xor ^= i
    return xor
#O(n) time
#O(1) space
