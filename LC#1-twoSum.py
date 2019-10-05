class Solution:
  def twoSum(self,nums, target):
    numsDict = {}
    for key,value in enumerate(nums):
      if target - value in numsDict:
        return [numsDict[target-value], key]
      else:
        numsDict[value] = key 
    return []
    
 #O(n) time
 #O(n) space
