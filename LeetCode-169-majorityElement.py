class Solution(object):
    def majorityElement(self, nums):
        count = 0
        result = 0
        for index, value in enumerate(nums):
            if count == 0:
                result = value
            if result == value:
                count += 1
            else:
                count -= 1
        return result
        
# O(n) time complexity
# O(1) space complexity
