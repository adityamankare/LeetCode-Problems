class Solution:
  def moveZeroes(self,nums):
    counter = 0
    for i in nums:
      if i != 0:
        nums[counter] = i
        counter += 1
    nums[counter:] = [0]*(len(nums)-counter)
    return nums
    
#O(n) time
#O(n) space
