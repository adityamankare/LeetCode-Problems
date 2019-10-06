from collections import Counter
class Solution:
  def isAnagram(self,s,t):
    if Counter(s) == Counter(t):
      return True
    else:
      return False
      
#O(n) time
#O(1) space
