class Solution:  
  def myAtoi(self,str):
  
    #remove padding spaces
    str = str.strip()
    
    #set up negative value boolean
    negative = False
    if str and str[0] == '-':
      negative = True
      
    #remove leading '+' or '-'
    if str and (str[0]== '+' or str[0] == '-'):
      str = str[1:]
      
    #return 0 if input is not a string
    if not str:
      return 0
      
    #create dictionary of digits
    digits = {i for i in '0123456789'}
    #declare the result variable
    result = 0
    
    #loop through string and convert to int
    for a in str:
      if a not in digits:
        break
      result = result*10 + int(a)
      
    #result if negative
    if negative:
      result = -result
      
    #return final result within range of -2**31 and 2**31
    result = max(min(result, 2**31-1),-2**31)
    return result
    
#O(n) time
#O(n) space
