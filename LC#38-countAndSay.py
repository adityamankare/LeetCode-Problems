class Solution:
  def countAndSay(self,n):
    sequence = [1]
    for i in range(n-1):
      nextNum = []
      for num in sequence:
        if (not nextNum) or (nextNum[-1] != num):
          nextNum += [1, num]
        else:
          nextNum[-2] += 1
      sequence = nextNum
    return "".join(map(str, sequence))
    
 #O(2^n) time
 #O(2^n) space
