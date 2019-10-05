from collections import Counter
class Solution:
  def intersect(self,nums1, nums2):
    freq = Counter(nums1)
    result = [] 
    for num in nums2: 
      if num in freq and freq[num] > 0:
        result.append(num)
        freq[num]-=1
    return result
    
#O(n) time
#O(n) space
