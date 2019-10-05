#BRUTE FORCE
class Solution:  
  def plusOne(self,digits):
    stringInput = ''.join(str(i) for i in digits)
    numberInput = int(stringInput) 
    incrementOne = numberInput + 1
    stringOutput = str(incrementOne)
    result = list(stringOutput)   
    return result
    
#SOLUTION
class Solution:  
  def plusOne(self,digits):
    i = len(digits)-1
    while digits[i] == 9:
      digits[i] = 0
      i -= 1
    if i == -1:
      return [1] + digits
    elif i == len(digits)-1:
      digits[-1] = digits[-1] + 1
      return digits
    else:
      digits[i] = digits[i] + 1
      return digits
#O(n) time
#O(1) space
