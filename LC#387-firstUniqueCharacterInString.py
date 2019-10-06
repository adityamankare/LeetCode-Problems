from collections import Counter
class Solution:
  def firstUniqChar(self,s):
    freq = Counter(s)
    for index, char in enumerate(s):
      if freq[char] == 1:
        return index
    return -1
    
#O(n) time
#O(n) space
