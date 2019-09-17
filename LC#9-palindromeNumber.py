class Solution(object):
  def isPalindrome(self, x):
    count = 0
    result = 0
    original = x

    if x < 0:
      return False

    while x!= 0:
      if count == 0:
        result = result*10 + x%10
        x//=10
    if result == original:
      return True
    else: 
      return False
