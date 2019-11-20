class Solution:  
  def maxProfit(self, prices):
    if prices == []:
      return 0
    base = prices[0]
    result = 0
    for i in range(0, len(prices)):
      if prices[i] > base:
        diff = prices[i] - base
        if diff > result:
          result = diff
      elif base >= prices[i]:
        base = prices[i]
    return result
