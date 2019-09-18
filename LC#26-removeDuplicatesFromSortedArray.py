class Solution:
  def removeDuplicates(self, nums):
    i = 0
    for j in range(len(nums)):
      if nums[i] < nums[j]:
        i += 1
        nums[i] = nums[j]
    return i + 1

#O(n) time
#O(1) space
